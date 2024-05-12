# Created by Jones at 2024/05/12 18:20
# leetgo: 1.4.7
# https://leetcode.cn/problems/find-the-minimum-cost-array-permutation/
# https://leetcode.cn/contest/weekly-contest-397/problems/find-the-minimum-cost-array-permutation/

from typing import *
from leetgo_py import *

from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from functools import cache, cmp_to_key, lru_cache, reduce
from heapq import heapify, heappop, heappush, heappushpop, heapreplace
from icecream import ic
from itertools import accumulate, chain, count, pairwise, zip_longest
from math import ceil, comb, floor, gcd, inf, isqrt, lcm, log2, perm, sqrt
from operator import xor
from pprint import pprint
from string import ascii_lowercase
from typing import List, Optional

# @lc code=begin


class Solution:
    def findPermutation(self, nums: List[int]) -> List[int]:
        """
        `score(perm) = |perm[0] - nums[perm[1]]| + ... `

        - `2 <= n == nums.length <= 14`
        - `nums` is a permutation of `[0, 1, 2, ..., n - 1]`.
        """


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().findPermutation(nums)
    print("\noutput:", serialize(ans, "integer[]"))
