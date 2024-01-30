# Created by Jones at 2024/01/30 21:01
# leetgo: dev
# https://leetcode.cn/problems/find-the-maximum-number-of-elements-in-subset/
# https://leetcode.cn/contest/weekly-contest-382/problems/find-the-maximum-number-of-elements-in-subset/

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
    def maximumLength(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        @cache
        def dfs(x:int):
            if cnt[x] == 0:
                return -1
            if cnt[x] == 1:
                return 1
            return 2 + dfs(x*x)
        
        res = cnt[1]
        if res & 1 == 0:
            res -= 1
        for x in cnt:
            if x == 1:
                continue
            res = max(res, dfs(x))
        return res
                    

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maximumLength(nums)
    print("\noutput:", serialize(ans, "integer"))
