# Created by Jones at 2024/03/15 12:41
# leetgo: 1.4.2
# https://leetcode.cn/problems/selling-pieces-of-wood/

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
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        p = [[0] * (n+1) for _ in range(m+1)]
        for x, y, price in prices:
            p[x][y] = price

        # enumerate the mid
        # dfs(m,n) =
        # max(dfs(m,y) + dfs(m,n-y) for y in range(n))
        # max(dfs(x,n) + dfs(m-x, n) for x in range(m))

        @cache
        def dfs(m, n):
            res = p[m][n]
            # try split to (m, y) (m, n-y)
            if n > 1:
                for y in range(1, n // 2 + 1):
                    res = max(res, dfs(m, y) + dfs(m, n - y))
            if m > 1:
                for x in range(1, m // 2 + 1):
                    res = max(res, dfs(x, n) + dfs(m - x, n))
            return res

        return dfs(m, n)


# @lc code=end

if __name__ == "__main__":
    m: int = deserialize("int", read_line())
    n: int = deserialize("int", read_line())
    prices: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().sellingWood(m, n, prices)
    print("\noutput:", serialize(ans, "long"))
