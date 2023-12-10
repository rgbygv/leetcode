# Created by Jones at 2023/12/10 16:15
# leetgo: dev
# https://leetcode.cn/problems/count-the-number-of-good-partitions/
# https://leetcode.cn/contest/weekly-contest-375/problems/count-the-number-of-good-partitions/

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
    def numberOfGoodPartitions(self, nums: List[int]) -> int:
        mod = 10**9 + 7
        # same should be the same

        first = {}
        last = {}
        for i, x in enumerate(nums):
            if x not in first:
                first[x] = i

        n = len(nums)

        for i in range(n - 1, -1, -1):
            x = nums[i]
            if x not in last:
                last[x] = i
        # print(first, last)
        cnt = 0
        l = r = 0
        while l < n:
            r = last[nums[l]]
            while l < r:
                r = max(r, last[nums[l]])
                l += 1
            # print(l, r)
            cnt += 1
            l += 1
        return pow(2, cnt - 1, mod)


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().numberOfGoodPartitions(nums)

    print("\noutput:", serialize(ans))
