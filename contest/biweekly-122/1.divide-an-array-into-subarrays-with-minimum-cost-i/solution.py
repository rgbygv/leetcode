# Created by Jones at 2024/01/20 22:30
# leetgo: dev
# https://leetcode.cn/problems/divide-an-array-into-subarrays-with-minimum-cost-i/
# https://leetcode.cn/contest/biweekly-contest-122/problems/divide-an-array-into-subarrays-with-minimum-cost-i/

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
    def minimumCost(self, nums: List[int]) -> int:
        return nums[0] + sum(sorted(nums[1:])[:2])


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minimumCost(nums)

    print("\noutput:", serialize(ans))
