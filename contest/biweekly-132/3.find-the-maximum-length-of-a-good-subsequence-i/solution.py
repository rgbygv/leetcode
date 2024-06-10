# Created by Jones at 2024/06/10 13:09
# leetgo: 1.4.7
# https://leetcode.cn/problems/find-the-maximum-length-of-a-good-subsequence-i/
# https://leetcode.cn/contest/biweekly-contest-132/problems/find-the-maximum-length-of-a-good-subsequence-i/

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
    def maximumLength(self, nums: List[int], k: int) -> int:
        """
        - `1 <= nums.length <= 500`
        - `1 <= nums[i] <= 10⁹`
        - `0 <= k <= min(nums.length, 25)`
        """

        @cache
        def dfs(i: int, k: int, last: int):
            if i < 0:
                return 0
            if k < 0:
                return -inf
            res = 0
            # choose
            if last == 0 or k - (nums[i] != last) >= 0:
                res = 1 + dfs(i - 1, k - (last != 0 and nums[i] != last), nums[i])
            # don't
            res = max(res, dfs(i - 1, k, last))
            return res

        res = dfs(len(nums) - 1, k, 0)
        dfs.cache_clear()
        return res


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().maximumLength(nums, k)
    print("\noutput:", serialize(ans, "integer"))
