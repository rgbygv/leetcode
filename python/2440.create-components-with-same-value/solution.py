# Created by Jones at 2023/11/04 21:09
# leetgo: dev
# https://leetcode.cn/problems/create-components-with-same-value/

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
    def componentValue(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        g = [[] for _ in range(n)]

        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        s = sum(nums)
        mx = max(nums)

        for num in range(mx, s + 1):
            if s % num != 0:
                continue
            if s // num > n:
                continue

            def dfs(x: int, fa: int):
                s = nums[x]
                for y in g[x]:
                    if y == fa:
                        continue
                    sub = dfs(y, x)
                    if sub == num:
                        continue
                    s += sub
                if s > num:
                    return inf
                return s

            if dfs(0, -1) != inf:
                # print(num, dfs(0, -1))
                return s // num - 1
        return 0


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().componentValue(nums, edges)

    print("\noutput:", serialize(ans))
