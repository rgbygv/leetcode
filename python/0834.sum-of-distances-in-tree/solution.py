# Created by Jones at 2024/04/28 19:43
# leetgo: 1.4.5
# https://leetcode.com/problems/sum-of-distances-in-tree/

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
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n)]

        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        size = [0] * n

        distance_sum = 0  # the root is 0

        def dfs(x, fa, d):
            # node `x`, his father is `fa`, his depth is `d`
            nonlocal distance_sum
            distance_sum += d
            for y in g[x]:
                if y == fa:
                    continue
                dfs(y, x, d + 1)
                size[x] += size[y]
            size[x] += 1

        dfs(0, -1, 0)

        res = [-1] * n

        def change_root(x, fa, distance_sum):
            for y in g[x]:
                if y == fa:
                    continue
                # change root to y
                # size[y] -= 1, (n-size[y] += 1
                cur = distance_sum + (n - size[y]) - size[y]
                res[y] = cur
                change_root(y, x, cur)

        res[0] = distance_sum
        change_root(0, -1, distance_sum)
        return res


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().sumOfDistancesInTree(n, edges)
    print("\noutput:", serialize(ans, "integer[]"))
