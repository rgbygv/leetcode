# Created by Jones at 2023/10/28 22:30
# leetgo: dev
# https://leetcode.cn/problems/subarrays-distinct-element-sum-of-squares-i/
# https://leetcode.cn/contest/biweekly-contest-116/problems/subarrays-distinct-element-sum-of-squares-i/

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
    def sumCounts(self, nums: List[int]) -> int:
        res = 0
        mod = 10**9 + 7
        n = len(nums)

        for i in range(n):
            s = set()
            for j in range(i, -1, -1):
                s.add(nums[j])
                res += len(s) ** 2

        return res % mod


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().sumCounts(nums)

    print("\noutput:", serialize(ans))
