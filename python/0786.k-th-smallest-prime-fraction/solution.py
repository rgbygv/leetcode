# Created by Jones at 2024/05/10 12:43
# leetgo: 1.4.7
# https://leetcode.com/problems/k-th-smallest-prime-fraction/

from typing import *
from leetgo_py import *

from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from functools import cache, cmp_to_key, lru_cache, reduce
from heapq import heapify, heappop, heappush, heappushpop, heapreplace
from icecream import ic
from itertools import accumulate, chain, count, pairwise, zip_longest
from math import ceil, comb, floor, gcd, inf, isqrt, lcm, log2, perm, sqrt
from operator import xor
from pprint import pprint
from string import ascii_lowercase
from typing import List, Optional

# @lc code=begin


class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        """
        - `2 <= arr.length <= 1000`
        - `1 <= arr[i] <= 3 * 10⁴`
        - `arr[0] == 1`
        - `arr[i]` is a **prime** number for `i > 0`.
        - All the numbers of `arr` are **unique** and sorted in **strictly increasing** order.
        - `1 <= k <= arr.length * (arr.length - 1) / 2`
        """

        def cmp(i, j):
            return 1 if arr[i[0]] * arr[j[1]] > arr[j[0]] * arr[i[1]] else -1

        i, j = sorted(
            ((i, j) for j in range(len(arr)) for i in range(j)),
            key=cmp_to_key(cmp),
        )[k - 1]
        return [arr[i], arr[j]]


# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().kthSmallestPrimeFraction(arr, k)
    print("\noutput:", serialize(ans, "integer[]"))
