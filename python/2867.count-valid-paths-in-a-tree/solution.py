# Created by Jones at 2024/02/27 12:39
# leetgo: 1.4.1
# https://leetcode.cn/problems/count-valid-paths-in-a-tree/

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
N = int(1e5) + 1
is_prime = [True] * N
is_prime[0] = is_prime[1] = False
for i in range(2, N):
    if is_prime[i]:
        for j in range(i + i, N, i):
            is_prime[j] = False


class Solution:
    def countPaths(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n + 1)]

        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        res = 0

        def dfs(x, fa):
            nonlocal res
            if is_prime[x]:
                cnt = 1
                for y in g[x]:
                    if y == fa:
                        continue
                    not_valid, valid = dfs(y, x)
                    res += cnt * not_valid
                    cnt += not_valid
                return [0, cnt]
            else:
                cnt = [1, 0]

                for y in g[x]:
                    if y == fa:
                        continue
                    not_valid, valid = dfs(y, x)
                    res += cnt[0] * valid + cnt[1] * not_valid
                    cnt[0] += not_valid
                    cnt[1] += valid
                return cnt

        dfs(1, 0)
        return res


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().countPaths(n, edges)
    print("\noutput:", serialize(ans, "long"))
