# Created by Jones at 2024/06/03 15:39
# leetgo: 1.4.7
# https://leetcode.cn/problems/shortest-subarray-with-or-at-least-k-ii/

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
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        res = inf
        for r, x in enumerate(nums):
            if x >= k:
                return 1
            l = r - 1
            while l >= 0 and nums[l] | x != nums[l]:
                nums[l] |= x
                if nums[l] >= k:
                    res = min(res, r - l + 1)
                    break
                l -= 1
        return res if res != inf else -1


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().minimumSubarrayLength(nums, k)
    print("\noutput:", serialize(ans, "integer"))
