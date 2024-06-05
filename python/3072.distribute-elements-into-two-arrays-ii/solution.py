# Created by Jones at 2024/06/05 12:54
# leetgo: 1.4.7
# https://leetcode.cn/problems/distribute-elements-into-two-arrays-ii/

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
from sortedcontainers import SortedList


class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        a = SortedList()  # nums1
        b = SortedList()  # nums2
        res1 = []
        res2 = []
        a.add((nums[0], 0))
        res1.append(nums[0])
        b.add((nums[1], 1))
        res2.append(nums[1])
        for idx in range(2, len(nums)):
            x = nums[idx]
            i = a.bisect_left((x, inf))
            j = b.bisect_left((x, inf))
            # ic(a, i, b, j)
            m, n = len(a), len(b)
            if m - i > n - j:
                a.add((x, idx))
                res1.append(x)
            elif m - i < n - j:
                b.add((x, idx))
                res2.append(x)
            elif m <= n:
                a.add((x, idx))
                res1.append(x)
            else:
                b.add((x, idx))
                res2.append(x)
        # ic(a, b)
        return res1 + res2


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().resultArray(nums)
    print("\noutput:", serialize(ans, "integer[]"))
