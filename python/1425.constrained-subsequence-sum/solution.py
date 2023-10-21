# Created by Jones at 2023/10/21 15:02
# leetgo: dev
# https://leetcode.cn/problems/constrained-subsequence-sum/

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
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        res = -inf

        q = deque()

        for i, x in enumerate(nums):
            while q and q[0][0] + k < i:
                q.popleft()
            cur = x + max(0, (0 if not q else q[0][1]))
            res = max(res, cur)
            while q and q[-1][1] <= cur:
                q.pop()
            q.append((i, cur))

        return res


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().constrainedSubsetSum(nums, k)

    print("\noutput:", serialize(ans))
