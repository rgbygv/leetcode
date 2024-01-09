# Created by Jones at 2024/01/09 20:52
# leetgo: dev
# https://leetcode.cn/problems/maximize-the-number-of-partitions-after-operations/
# https://leetcode.cn/contest/weekly-contest-379/problems/maximize-the-number-of-partitions-after-operations/

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


class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        if k == 26:
            return 1
        """
        aabcdaf  k=2

        def dfs(i:int, change:bool, k:int, mask:int):
            if k == 0:
            
            res = 0
            if change:
                res =  dfs(i+1,False,k-1)
            if mask >> s[i] & 1:
                res = max(res, dfs(i+1,change,k,mask)) 
            else:
                res = max(res, dfs(i+1,change,k-1,mask | (1<<s[i])))
            
        
        """


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().maxPartitionsAfterOperations(s, k)

    print("\noutput:", serialize(ans))
