# Created by Jones at 2024/04/27 13:28
# leetgo: 1.4.5
# https://leetcode.cn/problems/k-th-smallest-prime-fraction/

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
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        # - `2 <= arr.length <= 1000`
        # - `1 <= arr[i] <= 3 * 10⁴`
        # - `arr[0] == 1`
        # - `arr[i]` is a **prime** number for `i > 0`.
        # - All the numbers of `arr` are **unique** and sorted in **strictly increasing** order.
        # - `1 <= k <= arr.length * (arr.length - 1) / 2`

        """
        the simplest way is store all (i,j) and sort it, but it's slow

        q = []
        for i, x in enumerate(arr):
            for j in range(i + 1, len(arr)):
                q.append((x, arr[j]))

        def cmp(a, b):
            x = a[0] * b[1]
            y = a[1] * b[0]
            if x > y:
                return 1
            if x == y:
                return 0
            if x < y:
                return -1

        q.sort(key=cmp_to_key(cmp))
        return list(q[k - 1])
        """

        # we can know the smallest is (0, n-1)
        # how to use the condition: arr[i] is prime?
        # if we store ( a[i]/a[j], i, j) ,float is not good
        # so we store (divmod(a[j],a[i]), i, j), and we need the max divmod(a[j],a[i])
        class Frac:
            def __init__(self, idx: int, idy: int, x: int, y: int) -> None:
                self.idx = idx
                self.idy = idy
                self.x = x
                self.y = y

            def __lt__(self, other: "Frac") -> bool:
                return self.x * other.y < self.y * other.x

        n = len(arr)
        q = []
        for j in range(1, n):
            heappush(q, (Frac(0, j, arr[0], arr[j])))

        for _ in range(k - 1):
            frac = heappop(q)
            i, j = frac.idx, frac.idy
            if i + 1 < j:
                heappush(q, (Frac(i + 1, j, arr[i + 1], arr[j])))
        # print(q)
        frac = heappop(q)
        i, j = frac.idx, frac.idy
        return [arr[i], arr[j]]


# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().kthSmallestPrimeFraction(arr, k)
    print("\noutput:", serialize(ans, "integer[]"))
