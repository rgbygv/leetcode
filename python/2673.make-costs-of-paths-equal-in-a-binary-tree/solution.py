# Created by Jones at 2024/02/28 11:59
# leetgo: 1.4.1
# https://leetcode.cn/problems/make-costs-of-paths-equal-in-a-binary-tree/

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
    def minIncrements(self, n: int, cost: List[int]) -> int:
        res = 0

        def dfs(x):
            nonlocal res
            if x > n:
                return 0
            left, right = dfs(2 * x), dfs(2 * x + 1)
            if left < right:
                left, right = right, left
            res += left - right
            return left + cost[x - 1]

        dfs(1)
        return res


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    cost: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minIncrements(n, cost)
    print("\noutput:", serialize(ans, "integer"))
