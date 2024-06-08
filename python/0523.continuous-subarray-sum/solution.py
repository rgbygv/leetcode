# Created by Jones at 2024/06/08 12:10
# leetgo: 1.4.7
# https://leetcode.com/problems/continuous-subarray-sum/

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
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        mp = {0: 0}
        s = 0

        for i, x in enumerate(nums, 1):
            s = (s + x) % k
            if s in mp:
                if i - mp[s] > 1:
                    return True
            else:
                mp[s] = i
        return False


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().checkSubarraySum(nums, k)
    print("\noutput:", serialize(ans, "boolean"))
