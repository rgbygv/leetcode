# Created by Jones at 2023/12/09 22:30
# leetgo: dev
# https://leetcode.cn/problems/length-of-longest-subarray-with-at-most-k-frequency/
# https://leetcode.cn/contest/biweekly-contest-119/problems/length-of-longest-subarray-with-at-most-k-frequency/

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
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        cnt = Counter()
        # freq = Counter()
        l = 0
        res = 0
        for r, x in enumerate(nums):
            cnt[x] += 1
            # freq[cnt[x] - 1] -= 1
            # freq[cnt[x]] += 1
            while cnt[x] > k:
                cnt[nums[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().maxSubarrayLength(nums, k)

    print("\noutput:", serialize(ans))
