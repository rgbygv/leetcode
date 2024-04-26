# Created by Jones at 2024/04/26 23:23
# leetgo: 1.4.5
# https://leetcode.cn/problems/sum-of-mutated-array-closest-to-target/

from typing import *
from leetgo_py import *

from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from copy import deepcopy
from functools import cache, cmp_to_key, lru_cache, reduce
from heapq import heapify, heappop, heappush, heappushpop, heapreplace
from itertools import accumulate, chain, count, pairwise, zip_longest
from math import ceil, comb, floor, gcd, inf, isqrt, log2, perm, sqrt
from operator import xor
from pprint import pprint
from string import ascii_lowercase
from typing import List, Optional

# @lc code=begin


class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        # - `1 <= arr.length <= 10⁴`
        # - `1 <= arr[i], target <= 10⁵`
        arr.sort()
        p = list(accumulate(arr, initial=0))

        n = len(arr)
        i = n - 1

        res = [inf, inf]  # (diff, value)
        for x in range(min(arr[-1], target), -1, -1):
            while i >= 0 and arr[i] > x:
                i -= 1
            s = p[i + 1] + x * (n - 1 - i)
            if (d := abs(s - target)) <= res[0]:
                res = [d, x]
        return res[1]


# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().findBestValue(arr, target)
    print("\noutput:", serialize(ans, "integer"))
