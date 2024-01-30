# Created by Jones at 2024/01/30 21:01
# leetgo: dev
# https://leetcode.cn/problems/minimize-or-of-remaining-elements-using-operations/
# https://leetcode.cn/contest/weekly-contest-382/problems/minimize-or-of-remaining-elements-using-operations/

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
    def minOrAfterOperations(self, nums: List[int], k: int) -> int:
        N = 30
        res = 0
        mask = 0
        for i in range(N-1,-1,-1):
            mask |= 1 << i
            cnt = 0
            cur = -1
            for x in nums:
                cur &= x & mask
                if cur:
                    cnt += 1
                else:
                    cur = -1
            if cnt > k:
                res |= 1<<i
                mask ^= 1<<i
        return res
                    
                
        
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().minOrAfterOperations(nums, k)
    print("\noutput:", serialize(ans, "integer"))
