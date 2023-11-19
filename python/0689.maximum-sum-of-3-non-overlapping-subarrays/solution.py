# Created by Jones at 2023/11/19 12:00
# leetgo: dev
# https://leetcode.cn/problems/maximum-sum-of-3-non-overlapping-subarrays/

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
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        suf = []
        s = 0
        for i in range(2 * k, n):
            s += nums[i]
            if i >= 3 * k - 1:
                heappush(suf, (-s, i - (k - 1)))
                s -= nums[i - (k - 1)]

        ps = sum(nums[: k - 1])
        pre = []
        s = sum(nums[k : 2 * k - 1])
        key = 0
        val = None
        # print(suf)

        for mid in range(k - 1, n - k):
            s += nums[mid + k]
            ps += nums[mid]
            heappush(pre, (-ps, mid - (k - 1)))
            while suf and suf[0][1] <= mid + k:
                heappop(suf)
            if not suf:
                break
            cur = s - pre[0][0] - suf[0][0]
            cur_val = (pre[0][1], mid + 1, suf[0][1])
            if cur > key or cur == key and cur_val < val:
                key = cur
                val = cur_val

            s -= nums[mid + 1]
            ps -= nums[mid - (k - 1)]
        return list(val)


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().maxSumOfThreeSubarrays(nums, k)

    print("\noutput:", serialize(ans))
