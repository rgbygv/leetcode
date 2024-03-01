# Created by Jones at 2024/03/01 20:37
# leetgo: 1.4.1
# https://leetcode.cn/problems/steps-to-make-array-non-decreasing/

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
    def totalSteps(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        i = 0
        while i < n:
            # find increase (i, j)
            j = i + 1
            while j < n and nums[i] > nums[j]:
                j += 1
            # compute how to delete(a[i+1:j])
            # we should find the first a[x] > a[y] (x < y)
            st = [(i, 0)]
            for y in range(i + 1, j):
                max_t = 0
                while nums[y] >= nums[st[-1][0]]:
                    _, t = st.pop()
                    max_t = max(max_t, t)
                res = max(res, max_t + 1)
                st.append((y, max_t + 1))
            i = j
        return res


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().totalSteps(nums)
    print("\noutput:", serialize(ans, "integer"))
