# Created by Jones at 2023/11/05 10:30
# leetgo: dev
# https://leetcode.cn/problems/maximum-score-after-applying-operations-on-a-tree/
# https://leetcode.cn/contest/weekly-contest-370/problems/maximum-score-after-applying-operations-on-a-tree/

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
    def maximumScoreAfterOperations(
        self, edges: List[List[int]], values: List[int]
    ) -> int:
        n = len(values)

        g = [[] for _ in range(n)]

        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        @cache
        def dfs(x, fa):
            op1 = values[x]
            op2 = 0
            is_leaf = True
            for y in g[x]:
                if y == fa:
                    continue
                is_leaf = False
                s1, s2 = dfs(y, x)
                op1 += s1
                op2 += s2
            if op2 == 0 and is_leaf:
                op2 = -inf
            # print(x, op1, max(values[x] + op2, op1 - values[x]))
            return op1, max(values[x] + op2, op1 - values[x])

        op1, op2 = dfs(0, -1)
        return op2


# @lc code=end

if __name__ == "__main__":
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    values: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maximumScoreAfterOperations(edges, values)

    print("\noutput:", serialize(ans))
