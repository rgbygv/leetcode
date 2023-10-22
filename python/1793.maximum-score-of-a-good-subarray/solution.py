# Created by Jones at 2023/10/22 14:25
# leetgo: dev
# https://leetcode.cn/problems/maximum-score-of-a-good-subarray/

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
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)

        left = [0] * n
        right = [n - 1] * n

        # find the first j of a[j] > a[i]

        st = []

        for i, x in enumerate(nums):
            while st and x < nums[st[-1]]:
                right[st.pop()] = i - 1
            if st:
                left[i] = st[-1] + 1
            st.append(i)

        res = 0
        for i in range(n):
            l, r = left[i], right[i]
            if l <= k <= r:
                res = max(res, (r - l + 1) * nums[i])
        return res


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().maximumScore(nums, k)

    print("\noutput:", serialize(ans))
