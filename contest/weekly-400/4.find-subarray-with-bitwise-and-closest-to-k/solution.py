# Created by Jones at 2024/06/02 13:46
# leetgo: 1.4.7
# https://leetcode.cn/problems/find-subarray-with-bitwise-and-closest-to-k/
# https://leetcode.cn/contest/weekly-contest-400/problems/find-subarray-with-bitwise-and-closest-to-k/

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


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        """
        if nums[i] <= k then we can't add it
        """
        # del dup
        q = []
        for x in nums:
            if q and q[-1] == x:
                continue
            q.append(x)
        res = inf
        for i, x in enumerate(q):
            res = min(res, abs(x - k))
            for j in range(i - 1, -1, -1):
                if q[j] & x != q[j]:
                    q[j] &= x
                    res = min(res, abs(q[j] - k))
                else:
                    break

            # for j in range(i, n):
            #     x &= q[j]
            #     res = min(res, abs(x - k))
            #     if x <= k:
            #         break
        return res


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().minimumDifference(nums, k)
    print("\noutput:", serialize(ans, "integer"))
