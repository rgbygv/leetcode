# Created by Jones at 2023/10/28 22:30
# leetgo: dev
# https://leetcode.cn/problems/length-of-the-longest-subsequence-that-sums-to-target/
# https://leetcode.cn/contest/biweekly-contest-116/problems/length-of-the-longest-subsequence-that-sums-to-target/

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
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        dp = [-inf] * (target + 1)
        dp[0] = 0

        for x in nums:
            next = dp.copy()
            for y in range(target):
                if x + y > target:
                    break
                next[x + y] = max(next[x + y], dp[y] + 1)
            dp = next
        return dp[target] if dp[target] != -inf else -1


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().lengthOfLongestSubsequence(nums, target)

    print("\noutput:", serialize(ans))
