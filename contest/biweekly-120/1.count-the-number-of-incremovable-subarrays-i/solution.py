# Created by Jones at 2023/12/23 22:30
# leetgo: dev
# https://leetcode.cn/problems/count-the-number-of-incremovable-subarrays-i/
# https://leetcode.cn/contest/biweekly-contest-120/problems/count-the-number-of-incremovable-subarrays-i/

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
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        # n = len(nums)

        # res = 0
        # for i in range(n):
        #     for j in range(i + 1, n + 1):
        #         tmp = nums[:i] + nums[j:]
        #         if len(tmp) <= 1 or all(y > x for x, y in pairwise(tmp)):
        #             res += 1
        # return res
        n = len(nums)

        right = n - 2

        while right >= 0 and nums[right] < nums[right + 1]:
            right -= 1
        if right == -1:
            return n * (n + 1) // 2
        res = n - right
        right += 1

        for left in range(n):
            # print(left, res)
            if left > 0 and nums[left] <= nums[left - 1]:
                break
            while right < n and nums[right] <= nums[left]:
                right += 1

            res += n - right + 1
        return res

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().incremovableSubarrayCount(nums)

    print("\noutput:", serialize(ans))
