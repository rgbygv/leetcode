# Created by Jones at 2023/11/05 10:30
# leetgo: dev
# https://leetcode.cn/problems/find-champion-ii/
# https://leetcode.cn/contest/weekly-contest-370/problems/find-champion-ii/

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
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        deg = [0] * n
        for x, y in edges:
            deg[y] += 1

        idx = [i for i, d in enumerate(deg) if d == 0]
        if len(idx) != 1:
            return -1
        return idx[0]


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().findChampion(n, edges)

    print("\noutput:", serialize(ans))
