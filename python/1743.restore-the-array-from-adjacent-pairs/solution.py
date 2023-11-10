# Created by Jones at 2023/11/10 13:56
# leetgo: dev
# https://leetcode.cn/problems/restore-the-array-from-adjacent-pairs/

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
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        deg = defaultdict(int)
        g = defaultdict(list)
        for x, y in adjacentPairs:
            g[x].append(y)
            g[y].append(x)
            deg[x] += 1
            deg[y] += 1

        i = None
        for key, val in deg.items():
            if val == 1:
                i = key
                break
        res = []
        q = deque([(i, None)])
        while q:
            x, fa = q.popleft()
            res.append(x)
            for y in g[x]:
                if y != fa:
                    q.append((y, x))
        return res


# @lc code=end

if __name__ == "__main__":
    adjacentPairs: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().restoreArray(adjacentPairs)

    print("\noutput:", serialize(ans))
