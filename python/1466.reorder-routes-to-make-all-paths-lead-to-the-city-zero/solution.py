# Created by Jones at 2023/12/07 15:09
# leetgo: dev
# https://leetcode.cn/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/

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
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        seen = set()
        for x, y in connections:
            g[x].append(y)
            g[y].append(x)
            seen.add((x, y))

        q = deque([0])
        vis = [False] * n
        vis[0] = True
        res = 0
        while q:
            x = q.popleft()
            for y in g[x]:
                if vis[y]:
                    continue
                vis[y] = True
                if (y, x) not in seen:
                    res += 1
                q.append(y)
        return res


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    connections: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().minReorder(n, connections)

    print("\noutput:", serialize(ans))
