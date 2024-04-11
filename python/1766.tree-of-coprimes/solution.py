# Created by Jones at 2024/04/11 12:46
# leetgo: 1.4.5
# https://leetcode.cn/problems/tree-of-coprimes/

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
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        # `1 <= nums[i] <= 50`
        n = len(nums)

        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        # calculate the coprime of 1..=50
        N = 50
        prime = [[] for _ in range(N + 1)]
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                if gcd(i, j) == 1:
                    prime[i].append(j)

        last = [[] for _ in range(N + 1)]
        res = [-1] * n

        def dfs(x: int, fa: int, d: int):
            for y in g[x]:
                if y == fa:
                    continue
                # x is y's ancestor
                last[nums[x]].append((x, d))
                k = -1
                max_depth = -1
                for z in prime[nums[y]]:
                    if last[z]:
                        fa, depth = last[z][-1]
                        # find the closest ancstor
                        if depth > max_depth:
                            k = fa
                            max_depth = depth
                res[y] = k
                dfs(y, x, d + 1)
                last[nums[x]].pop()

        dfs(0, -1, 0)
        return res


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().getCoprimes(nums, edges)
    print("\noutput:", serialize(ans, "integer[]"))
