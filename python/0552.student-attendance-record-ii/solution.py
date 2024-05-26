# Created by Jones at 2024/05/26 14:11
# leetgo: 1.4.7
# https://leetcode.com/problems/student-attendance-record-ii/

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
    def checkRecord(self, n: int) -> int:
        """
        - The student was absent ( `'A'`) for **strictly** fewer than 2 days **total**.
        - The student was **never** late ( `'L'`) for 3 or more **consecutive** days.
        """
        mod = 10**9 + 7
        dp = [[[0] * 3 for _ in range(2)] for _ in range(n + 1)]
        for A in range(2):
            for L in range(3):
                dp[n][A][L] = 1
        for i in range(n - 1, -1, -1):
            for A in range(1, -1, -1):
                for L in range(2, -1, -1):
                    # present
                    dp[i][A][L] = dp[i + 1][A][0]
                    # absent
                    if A == 0:
                        dp[i][A][L] += dp[i + 1][A + 1][0]
                    # late
                    if L < 2:
                        dp[i][A][L] += dp[i + 1][A][L + 1]
                    dp[i][A][L] %= mod

        return dp[0][0][0]

        @cache
        def dfs(i: int, A: int, L: int):
            if i == n:
                return 1
            # present
            res = dfs(i + 1, A, 0)
            # absent
            if A == 0:
                res += dfs(i + 1, A + 1, 0)
            # late
            if L < 2:
                res += dfs(i + 1, A, L + 1)
            return res % mod

        return dfs(0, 0, 0)


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().checkRecord(n)
    print("\noutput:", serialize(ans, "integer"))
