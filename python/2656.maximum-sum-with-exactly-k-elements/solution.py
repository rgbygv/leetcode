# Created by Jones at 2023/11/15 19:22
# leetgo: dev
# https://leetcode.cn/problems/maximum-sum-with-exactly-k-elements/

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
    def maximizeSum(self, nums: List[int], k: int) -> int:
        x = max(nums)
        return (x + x + k - 1) * k // 2


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().maximizeSum(nums, k)

    print("\noutput:", serialize(ans))
