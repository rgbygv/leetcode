# Created by Jones at 2023/10/26 19:31
# leetgo: dev
# https://leetcode.cn/problems/binary-trees-with-factors/

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
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        mod = 10**9 + 7
        s = set(arr)

        @cache
        def dfs(x: int):
            res = 1
            for left in s:
                if x % left == 0 and x // left in s:
                    res += dfs(left) * dfs(x // left)
            return res % mod

        return sum(dfs(x) for x in s) % mod


# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    ans = Solution().numFactoredBinaryTrees(arr)

    print("\noutput:", serialize(ans))
