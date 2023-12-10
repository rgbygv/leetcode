# Created by Jones at 2023/12/10 16:15
# leetgo: dev
# https://leetcode.cn/problems/count-subarrays-where-max-element-appears-at-least-k-times/
# https://leetcode.cn/contest/weekly-contest-375/problems/count-subarrays-where-max-element-appears-at-least-k-times/

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
    def countSubarrays(self, nums: List[int], k: int) -> int:
        x = max(nums)
        q = []
        for i, y in enumerate(nums):
            if y == x:
                q.append(i)
        if len(q) < k:
            return 0
        # print(q)
        q.append(len(nums))
        res = 0
        for r in range(k - 1, len(q) - 1):
            left = q[r - (k - 1)] + 1
            right = q[r + 1] - q[r]
            res += left * right
        return res


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().countSubarrays(nums, k)

    print("\noutput:", serialize(ans))
