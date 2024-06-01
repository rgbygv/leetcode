# Created by Jones at 2024/06/01 12:47
# leetgo: 1.4.7
# https://leetcode.cn/problems/number-of-ways-to-arrive-at-destination/

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
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        """
        - `1 <= n <= 200`
        - `n - 1 <= roads.length <= n * (n - 1) / 2`
        - `roads[i].length == 3`
        - `0 <= uᵢ, vᵢ <= n - 1`
        - `1 <= timeᵢ <= 10⁹`
        - `uᵢ != vᵢ`
        - There is at most one road connecting any two intersections.
        - You can reach any intersection from any other intersection.
        """
        mod = 10**9 + 7
        g = [[] for _ in range(n)]
        for x, y, t in roads:
            g[x].append((y, t))
            g[y].append((x, t))

        dist = [inf] * n
        q = [(0, 0)]
        f = [1] * n
        while q:
            d, x = heappop(q)
            for y, t in g[x]:
                if dist[y] >= (nd := d + t):
                    if dist[y] > nd:
                        dist[y] = nd
                        heappush(q, (nd, y))
                        f[y] = f[x]
                    else:
                        f[y] += f[x]
        return f[-1] % mod


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    roads: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().countPaths(n, roads)
    print("\noutput:", serialize(ans, "integer"))
