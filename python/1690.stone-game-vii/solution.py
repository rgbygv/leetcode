# Created by Jones at 2024/02/03 11:27
# leetgo: 1.4.1
# https://leetcode.cn/problems/stone-game-vii/

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
    def stoneGameVII(self, stones: List[int]) -> int:
        p = list(accumulate(stones, initial=0))
        n = len(stones)
        # f(l,r) = max(sum(l+1,r) - f(l+1,r), sum(l,r-1) - f(l,r-1))

        # @cache  
        # def f(l:int, r:int):
        #     # print(l,r)
        #     if l == r:
        #         return 0
        #     return max(p[r+1] - p[l+1] - f(l+1,r), p[r] - p[l] - f(l,r-1))

        # res= f(0, n-1)
        # f.cache_clear()
        # return res
        
        f = [[0] * n for _ in range(n)]
        
        for l in reversed(range(n)):
            for r in range(l+1,n):
                f[l][r] = max(p[r+1] - p[l+1] - f[l+1][r], p[r] - p[l] - f[l][r-1])
        return f[0][n-1]
# @lc code=end

if __name__ == "__main__":
    stones: List[int] = deserialize("List[int]", read_line())
    ans = Solution().stoneGameVII(stones)
    print("\noutput:", serialize(ans, "integer"))
