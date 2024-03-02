# Created by Jones at 2024/03/02 13:44
# leetgo: 1.4.1
# https://leetcode.cn/problems/reachable-nodes-with-restrictions/

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
    def reachableNodes(
        self, n: int, edges: List[List[int]], restricted: List[int]
    ) -> int:
        g = [[] for _ in range(n)]
        ban = set(restricted)
        for x, y in edges:
            if x not in ban and y not in ban:
                g[x].append(y)
                g[y].append(x)

        f = [False] * n

        def dfs(x, fa):
            if f[x]:
                return
            f[x] = True
            for y in g[x]:
                if y == fa:
                    continue
                dfs(y, x)

        dfs(0, -1)
        return sum(f)


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    restricted: List[int] = deserialize("List[int]", read_line())
    ans = Solution().reachableNodes(n, edges, restricted)
    print("\noutput:", serialize(ans, "integer"))
