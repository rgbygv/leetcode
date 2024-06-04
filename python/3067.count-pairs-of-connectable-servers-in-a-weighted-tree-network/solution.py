# Created by Jones at 2024/06/04 11:45
# leetgo: 1.4.7
# https://leetcode.cn/problems/count-pairs-of-connectable-servers-in-a-weighted-tree-network/

from typing import *
from leetgo_py import *

from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from functools import cache, cmp_to_key, lru_cache, reduce
from heapq import heapify, heappop, heappush, heappushpop, heapreplace
from icecream import ic
from itertools import accumulate, chain, count, pairwise, zip_longest
from math import ceil, comb, floor, gcd, inf, isqrt, lcm, log2, perm, sqrt
from operator import xor
from pprint import pprint
from string import ascii_lowercase
from typing import List, Optional

# @lc code=begin


class Solution:
    def countPairsOfConnectableServers(
        self, edges: List[List[int]], signalSpeed: int
    ) -> List[int]:
        n = len(edges) + 1
        g = [[] for _ in range(n)]
        for x, y, w in edges:
            g[x].append((y, w))
            g[y].append((x, w))

        def dfs(x: int, fa: int, p):
            nonlocal res
            s = 0
            for y, w in g[x]:
                if y == fa:
                    continue
                cnt = dfs(y, x, (p + w) % signalSpeed)
                if fa == -1:
                    res += s * cnt
                s += cnt
                # ic(x, y, cnt, res)
            return s + int(p == 0)

        ans = []
        for i in range(n):
            res = 0
            dfs(i, -1, 0)
            ans.append(res)

        return ans


# @lc code=end

if __name__ == "__main__":
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    signalSpeed: int = deserialize("int", read_line())
    ans = Solution().countPairsOfConnectableServers(edges, signalSpeed)
    print("\noutput:", serialize(ans, "integer[]"))
