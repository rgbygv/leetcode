# Created by Jones at 2024/04/27 19:47
# leetgo: 1.4.5
# https://leetcode.cn/problems/new-21-game/

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
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        # - `0 <= k <= n <= 10⁴`
        # - `1 <= maxPts <= 10⁴`

        if k - 1 + maxPts < n:
            return 1

        # @cache
        # def dfs(points: int):
        #     # points + x >= n => x >= n-points
        #     # have n-k..maxPts
        #     if points >= k:
        #         return points <= n

        #     res = 0
        #     for x in range(1, maxPts + 1):
        #         res += dfs(points + x)
        #     return res / maxPts

        # return dfs(0)

        f = [0] * (n + k + maxPts + 1)
        s = 0
        r = n + k + maxPts

        for x in range(n + k + maxPts, -1, -1):
            if x >= k:
                f[x] = int(x <= n)
            else:
                # f[x] = sum(f[x + 1 : x + maxPts + 1]) / maxPts
                f[x] = s / maxPts
            s += f[x]
            if r - x > maxPts:
                s -= f[x + maxPts]
        # print(f)

        return f[0]

        # f = [0] * (n + 1)
        # f[0] = 1
        # p = [0]
        # s = 1

        # for i in range(1, n + 1):
        #     # f[i] = sum(f[i - maxPts :])
        #     f[i] = (p[-1] - p[max(0, i - maxPts)]) / min(i, maxPts)
        #     s += f[i]
        #     p.append(s)
        # print(f)

        # return sum(f[k : n + 1])


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    k: int = deserialize("int", read_line())
    maxPts: int = deserialize("int", read_line())
    ans = Solution().new21Game(n, k, maxPts)
    print("\noutput:", serialize(ans, "double"))
