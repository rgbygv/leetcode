# Created by Jones at 2024/02/06 12:44
# leetgo: 1.4.1
# https://leetcode.cn/problems/p0NxJO/

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
from pprint import pprint
from string import ascii_lowercase
from typing import List, Optional

# @lc code=begin

class Solution:
    def magicTower(self, nums: List[int]) -> int:
        if sum(nums) < 0:
            return -1
        # we only put the neg to last
        # when sum became neg, we need move the min(neg) to last
        
        res = 0
        s = 1
        mn = []
        for x in nums:
            if x < 0:
                heappush(mn, x)
            s += x
            if s <= 0:
                if not mn or s - mn[0] <= 0:
                    return -1
                res += 1
                s -= heappop(mn)
        return res


            



# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().magicTower(nums)
    print("\noutput:", serialize(ans, "integer"))
