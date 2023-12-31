# Created by Bob at 2023/12/31 15:57
# leetgo: dev
# https://leetcode.cn/problems/check-if-bitwise-or-has-trailing-zeros/
# https://leetcode.cn/contest/weekly-contest-378/problems/check-if-bitwise-or-has-trailing-zeros/

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


class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        return sum(x & 1 == 0 for x in nums) >= 2


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().hasTrailingZeros(nums)

    print("\noutput:", serialize(ans))
