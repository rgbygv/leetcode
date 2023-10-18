# Created by Jones at 2023/10/18 12:34
# leetgo: dev
# https://leetcode.cn/problems/maximal-score-after-applying-k-operations/

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
    def maxKelements(self, nums: List[int], k: int) -> int:
        q = []
        for x in nums:
            heappush(q, -x)

        res = 0
        for _ in range(k):
            x = -heappop(q)
            if x == 0:
                break
            res += x
            heappush(q, -ceil(x / 3))
        return res


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().maxKelements(nums, k)

    print("\noutput:", serialize(ans))
