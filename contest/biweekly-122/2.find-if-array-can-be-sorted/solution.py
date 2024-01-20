# Created by Jones at 2024/01/20 22:30
# leetgo: dev
# https://leetcode.cn/problems/find-if-array-can-be-sorted/
# https://leetcode.cn/contest/biweekly-contest-122/problems/find-if-array-can-be-sorted/

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
    def canSortArray(self, nums: List[int]) -> bool:
        n = len(nums)
        i = 0
        while i < n:
            j = i + 1
            while j < n and nums[j].bit_count() == nums[i].bit_count():
                j += 1
            nums[i:j] = sorted(nums[i:j])
            i = j
        return nums == sorted(nums)
        # n = len(nums)
        # sl = sorted(nums)
        # for i, x in enumerate(sl):
        #     if x == nums[i]:
        #         continue
        #     j = i + 1
        #     cur = x.bit_count()
        #     while j < n and nums[j].bit_count() == cur and nums[j] != x:
        #         j += 1
        #     if nums[j] != x:
        #         return False
        #     nums[i], nums[j] = nums[i], nums[j]

        # return nums == sl
        # mp = defaultdict(list)

        # for x in nums:
        #     mp[x.bit_count()].append(x)

        # for key in mp:
        #     mp[key].sort(reverse=True)

        # pprint(mp)
        # for i in range(len(nums)):
        #     key = nums[i].bit_count()
        #     nums[i] = mp[key].pop()

        # return nums == sorted(nums)


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().canSortArray(nums)

    print("\noutput:", serialize(ans))
