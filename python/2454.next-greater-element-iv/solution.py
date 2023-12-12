# Created by Jones at 2023/12/12 11:35
# leetgo: dev
# https://leetcode.cn/problems/next-greater-element-iv/

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
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        st = []
        first = []
        n = len(nums)
        res = [-1] * n
        for i, x in enumerate(nums):
            while first and x > nums[first[-1]]:
                res[first.pop()] = x
            tmp = []
            while st and x > nums[st[-1]]:
                tmp.append(st.pop())
            first += tmp[::-1]
            st.append(i)
        return res


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().secondGreaterElement(nums)

    print("\noutput:", serialize(ans))
