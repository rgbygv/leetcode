# Created by Jones at 2023/11/06 20:04
# leetgo: dev
# https://leetcode.cn/problems/maximum-score-of-a-node-sequence/

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
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        n = len(scores)
        g = [[] for _ in range(n)]

        for x, y in edges:
            s = scores[x] + scores[y]
            g[x].append((y, s))
            g[y].append((x, s))

        for i in range(n):
            g[i].sort(key=lambda e: -e[1])

        res = -1
        # a - b - c - d
        # let's enum b and c

        for x, y in edges:
            # find max(b-a) + max(c-d) and a != c != d != b
            A = []
            for a, s in g[x]:
                if a != y:
                    A.append((a, s))
                    if len(A) >= 3:
                        break
            B = []
            for b, s in g[y]:
                if b != x:
                    B.append((b, s))
                    if len(B) >= 3:
                        break

            for a, s1 in A:
                for b, s2 in B:
                    s = s1 + s2
                    if a != b and s > res:
                        # print(x, y, a, b, s)
                        res = s
        return res


# @lc code=end

if __name__ == "__main__":
    scores: List[int] = deserialize("List[int]", read_line())
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().maximumScore(scores, edges)

    print("\noutput:", serialize(ans))
