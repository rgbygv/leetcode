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
        res = reduce(lambda x,y: x|y, nums)
        N = res.bit_length()
        
        n = len(nums)
        need = [-1] * (n+1)

        def valid(i:int):
            return all(need[i] != -1 for i in rang(i-1,i+2))
        for i in range(N-1,-1,-1):
            # check if res[i] can be 0
            if res >> i & 1 == 0:
                continue
            v = [j for j,x in enumerate(nums) if x >> i & 1 and valid(j)]
            if v == n:
                continue
            if len(v) < k:
                k -= len(v)
                for j in v:
                    need[j] = i
            

        return res
            
            


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().minOrAfterOperations(nums, k)
    print("\noutput:", serialize(ans, "integer"))
