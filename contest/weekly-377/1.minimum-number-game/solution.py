# Created by Jones at 2023/12/24 22:16
# leetgo: dev
# https://leetcode.cn/problems/minimum-number-game/
# https://leetcode.cn/contest/weekly-contest-377/problems/minimum-number-game/

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
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()

        res = []
        for i in range(1, len(nums), 2):
            res.append(nums[i])
            res.append(nums[i - 1])
        return res


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().numberGame(nums)

    print("\noutput:", serialize(ans))
