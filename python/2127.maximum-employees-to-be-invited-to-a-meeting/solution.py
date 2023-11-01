# Created by Jones at 2023/11/01 20:07
# leetgo: dev
# https://leetcode.cn/problems/maximum-employees-to-be-invited-to-a-meeting/

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
from string import ascii_lowercase
from typing import List, Optional

# @lc code=begin
# from sortedcontainers import SortedList


class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        deg = [0] * n
        rg = [[] for _ in range(n)]

        for x, y in enumerate(favorite):
            deg[y] += 1

        q = deque(i for i, d in enumerate(deg) if d == 0)
        while q:
            x = q.popleft()
            y = favorite[x]
            deg[y] -= 1
            # only not in cycle can append edge
            rg[y].append(x)
            if deg[y] == 0:
                q.append(y)

        res = 0
        res2 = 0

        for x in range(n):
            if deg[x] == 0:
                continue
            # now x must be in a cycle
            cnt = 0
            while deg[x] != 0:
                cnt += 1
                # visited
                deg[x] = 0
                x = favorite[x]

            if cnt == 2:
                # can add 2 egde point to cycle
                @cache
                def dfs(x):
                    res = 1
                    for y in rg[x]:
                        res = max(res, 1 + dfs(y))
                    return res

                res2 += dfs(favorite[x]) + dfs(x)
            else:
                res = max(res, cnt)
        return max(res, res2)


# @lc code=end

if __name__ == "__main__":
    favorite: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maximumInvitations(favorite)

    print("\noutput:", serialize(ans))
