# Created by Jones at 2023/10/31 15:26
# leetgo: dev
# https://leetcode.cn/problems/smallest-missing-genetic-value-in-each-subtree/

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
    def smallestMissingValueSubtree(
        self, parents: List[int], nums: List[int]
    ) -> List[int]:
        n = len(nums)
        mp = {v: i for i, v in enumerate(nums)}
        res = [1] * n

        if 1 not in mp:
            return res

        g = [[] for _ in range(n)]

        for i, fa in enumerate(parents):
            if fa != -1:
                g[fa].append(i)

        vis = set()

        def dfs(x):
            vis.add(nums[x])
            for y in g[x]:
                if nums[y] not in vis:
                    dfs(y)

        mex = 2
        x = mp[1]

        while x != -1:
            dfs(x)
            while mex in vis:
                mex += 1
            res[x] = mex
            x = parents[x]

        return res


# @lc code=end

if __name__ == "__main__":
    parents: List[int] = deserialize("List[int]", read_line())
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().smallestMissingValueSubtree(parents, nums)

    print("\noutput:", serialize(ans))
