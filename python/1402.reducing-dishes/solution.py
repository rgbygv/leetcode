# Created by Jones at 2023/10/22 14:12
# leetgo: dev
# https://leetcode.cn/problems/reducing-dishes/

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
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()

        @cache
        def dfs(i: int, k: int):
            if i == len(satisfaction):
                return 0

            op1 = satisfaction[i] * k + dfs(i + 1, k + 1)
            op2 = dfs(i + 1, k)
            return max(op1, op2)

        return dfs(0, 1)


# @lc code=end

if __name__ == "__main__":
    satisfaction: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxSatisfaction(satisfaction)

    print("\noutput:", serialize(ans))
