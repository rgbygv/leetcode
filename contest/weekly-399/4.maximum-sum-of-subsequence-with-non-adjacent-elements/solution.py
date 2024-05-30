# Created by Jones at 2024/05/30 19:14
# leetgo: 1.4.7
# https://leetcode.cn/problems/maximum-sum-of-subsequence-with-non-adjacent-elements/
# https://leetcode.cn/contest/weekly-contest-399/problems/maximum-sum-of-subsequence-with-non-adjacent-elements/

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
    def maximumSumSubsequence(self, nums: List[int], queries: List[List[int]]) -> int:
        """
        - `1 <= nums.length <= 5 * 10⁴`
        - `-10⁵ <= nums[i] <= 10⁵`
        - `1 <= queries.length <= 5 * 10⁴`
        - `queries[i] == [posᵢ, xᵢ]`
        - `0 <= posᵢ <= nums.length - 1`
        - `-10⁵ <= xᵢ <= 10⁵`
        """
        mod = 10 ** 9 + 7


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    queries: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().maximumSumSubsequence(nums, queries)
    print("\noutput:", serialize(ans, "integer"))
