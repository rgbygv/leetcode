# Created by Jones at 2023/10/29 10:30
# leetgo: dev
# https://leetcode.cn/problems/minimum-increment-operations-to-make-array-beautiful/
# https://leetcode.cn/contest/weekly-contest-369/problems/minimum-increment-operations-to-make-array-beautiful/

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
    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)

        @cache
        def dfs(i: int, j: int):
            if i >= n:
                return 0

            # must increase
            if j == 2:
                return max(0, k - nums[i]) + dfs(i + 1, 0)
            # increase
            op1 = max(0, k - nums[i]) + dfs(i + 1, 0)
            # dont increase
            op2 = dfs(i + 1, j + 1)

            return min(op1, op2)

        return dfs(0, 0)


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().minIncrementOperations(nums, k)

    print("\noutput:", serialize(ans))
