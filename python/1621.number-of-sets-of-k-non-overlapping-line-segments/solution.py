# Created by Jones at 2024/05/08 15:25
# leetgo: 1.4.6
# https://leetcode.cn/problems/number-of-sets-of-k-non-overlapping-line-segments/

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
    def numberOfSets(self, n: int, k: int) -> int:
        """
        - `2 <= n <= 1000`
        - `1 <= k <= n-1`
        """
        mod = 10**9 + 7

        f = [[0] * (n + 1) for _ in range(k)]
        f[0] = [x * (x - 1) // 2 for x in range(n + 1)]
        for i in range(1, k):
            p = list(accumulate(f[i - 1], initial=0))
            for j in range(i + 1, n + 1):
                """
                f[i][j+1] - f[i][j] = 
                sum(f[i-1][max(2, i), j])
                + f[i-1][j]   
                """
                # for mid in range(max(2, i), j):
                #     f[i][j] += f[i - 1][mid] * (j - mid) % mod
                #     f[i][j] %= mod
                f[i][j] = f[i][j - 1] + f[i - 1][j - 1] + p[j - 1] - p[max(2, i)]
                f[i][j] %= mod

        return f[-1][-1]

        # @cache
        # def dfs(k: int, n: int):
        #     if k == 1:
        #         return n * (n - 1) // 2
        #     res = 0
        #     for mid in range(min(2, k), n):
        #         res += dfs(k - 1, mid) * (n - mid ) % mod
        #         res %= mod
        #     # ic(k, n ,res)
        #     return res

        # return dfs(k, n)


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().numberOfSets(n, k)
    print("\noutput:", serialize(ans, "integer"))
