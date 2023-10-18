# Created by Jones at 2023/10/18 12:38
# leetgo: dev
# https://leetcode.cn/problems/parallel-courses-iii/

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
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        deg = [0] * n
        g = [[] for _ in range(n)]
        for x, y in relations:
            x -= 1
            y -= 1
            deg[y] += 1
            g[x].append(y)

        q = deque([i for i, d in enumerate(deg) if d == 0])

        res = 0
        dist = [0] * n

        while q:
            x = q.popleft()
            res = max(res, dist[x] + time[x])
            for y in g[x]:
                dist[y] = max(dist[y], dist[x] + time[x])
                deg[y] -= 1
                if deg[y] == 0:
                    q.append(y)

        return res


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    relations: List[List[int]] = deserialize("List[List[int]]", read_line())
    time: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minimumTime(n, relations, time)

    print("\noutput:", serialize(ans))
