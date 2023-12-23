# Created by Jones at 2023/12/23 22:30
# leetgo: dev
# https://leetcode.cn/problems/find-number-of-coins-to-place-in-tree-nodes/
# https://leetcode.cn/contest/biweekly-contest-120/problems/find-number-of-coins-to-place-in-tree-nodes/

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
    def placedCoins(self, edges: List[List[int]], cost: List[int]) -> List[int]:
        n = len(cost)
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        # print(sorted((x for x in cost), key=abs)[-3:])
        res = [0] * n

        def dfs(x, fa):
            max_q = []  # record the maxium pos
            min_q = []  # record the minimal neg
            if cost[x] > 0:
                max_q.append(cost[x])
            else:
                min_q.append(-cost[x])
            for y in g[x]:
                if y == fa:
                    continue
                sub1, sub2 = dfs(y, x)
                for xx in sub1:
                    heappush(max_q, xx)
                    if len(max_q) > 3:
                        heappop(max_q)

                for xx in sub2:
                    heappush(min_q, xx)
                    if len(min_q) > 3:
                        heappop(min_q)

            if len(max_q) + len(min_q) >= 3:
                score = 0
                if len(max_q) == 3:
                    score = max(score, max_q[0] * max_q[1] * max_q[2])
                if len(max_q) > 0 and len(min_q) >= 2:
                    tmp = None
                    if len(min_q) == 3:
                        tmp = heappop(min_q)
                    score = max(score, max(max_q) * min_q[0] * min_q[1])
                    if tmp is not None:
                        heappush(min_q, tmp)
            else:
                score = 1
            res[x] = score
            # print(x, max_q, min_q)
            return max_q, min_q

        dfs(0, -1)
        return res


# @lc code=end

if __name__ == "__main__":
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    cost: List[int] = deserialize("List[int]", read_line())
    ans = Solution().placedCoins(edges, cost)

    print("\noutput:", serialize(ans))
