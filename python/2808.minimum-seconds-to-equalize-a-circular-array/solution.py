# Created by Jones at 2024/01/30 15:49
# leetgo: dev
# https://leetcode.cn/problems/minimum-seconds-to-equalize-a-circular-array/

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
    def minimumSeconds(self, nums: List[int]) -> int:
        if len(set(nums)) == 1:
            return 0

        mp = defaultdict(list)
        for i,x in enumerate(nums):
            mp[x].append(i)
        
        res = n = len(nums)
        for v in mp.values():
            if len(v) == 1:
                continue
            v.append(n + v[0])
            
            cur = max(y - x for x, y in pairwise(v))
            res = min(res, cur)
            
        return res // 2
        


    
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minimumSeconds(nums)
    print("\noutput:", serialize(ans, "integer"))
