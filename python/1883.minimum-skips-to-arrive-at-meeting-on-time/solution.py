# Created by Jones at 2024/04/19 12:45
# leetgo: 1.4.5
# https://leetcode.cn/problems/minimum-skips-to-arrive-at-meeting-on-time/

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
    def minSkips(self, dist: List[int], speed: int, hoursBefore: int) -> int:
        s = sum(dist)
        if s > speed * hoursBefore:
            return -1

        n = len(dist)

        def calc(x: int):
            return (x + speed - 1) // speed * speed

        # p = list(accumulate((calc(x) for x in dist), initial=0))

        @cache
        def dfs(skip: int, i: int):
            if i == -1:
                return 0
            # if skip == 0:
            #     return p[i + 1]
            op1 = inf
            # skip dist[i]
            if skip > 0:
                op1 = dfs(skip - 1, i - 1) + dist[i]
            # don't skip
            op2 = calc(
                dfs(skip, i - 1) + dist[i]
            )  # why should calc dfs(skip, i-1) + dist[i] at same time?
            return min(op1, op2)

        for skip in range(n):
            min_dist = dfs(skip, n - 2) + dist[-1]
            if min_dist <= hoursBefore * speed:
                return skip
        return -1

        # @cache
        # def dfs(i: int, j: int):
        #     if i == j:
        #         return calc(dist[i])
        #     # we can merge any index between (i,j)

        # return dfs(0, n - 1)

        # f[i][j] : dist[..=i] use `j` skip can rest how much time
        # f[i][j] = min (f[k][j-1] - calc(k,i))

        # f = [[hoursBefore] * n for _ in range(n)]
        # for i in range(1,n+1):

        # for x in range(n):
        #     if f[-1][x] >= 0:
        #         return x
        # return -1

        # for i in range(n):
        #     if check(dist):
        #         return i
        # find the

        # @cache
        # def dfs(i: int, pre: int, t: int):
        #     # print(i, pre, t)
        #     if t < 0:
        #         return inf
        #     if i == n:
        #         return 0 if t * speed >= pre else inf
        #     # skip this
        #     op1 = 1 + dfs(i + 1, pre + dist[i], t)
        #     # don't skip this
        #     op2 = dfs(i + 1, 0, t - (pre + dist[i] + speed - 1) // speed)
        #     # print(i, pre, t, op1, op2)
        #     return min(op1, op2)

        # we have checked res is not -1

        # res = dfs(0, 0, hoursBefore)
        # if res == inf:
        #     return -1
        # return res

        # return dfs(0, 0, hoursBefore)


# @lc code=end

if __name__ == "__main__":
    dist: List[int] = deserialize("List[int]", read_line())
    speed: int = deserialize("int", read_line())
    hoursBefore: int = deserialize("int", read_line())
    ans = Solution().minSkips(dist, speed, hoursBefore)
    print("\noutput:", serialize(ans, "integer"))
