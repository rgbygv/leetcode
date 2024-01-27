# Created by Jones at 2024/01/27 16:22
# leetgo: dev
# https://leetcode.cn/problems/maximum-number-of-alloys/

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
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:
        # n = 3, k = 2, budget = 15, composition = [[1,1,1],[1,1,10]], stock = [0,0,100], cost = [1,2,3]
        
        def f(a:list[int]):
            l = 0
            r = int(1e9) + 5
            while l <= r:
                mid = (l+r) >> 1
                def check(mid):
                    cnt = 0
                    for i,x in enumerate(stock):
                        need = mid * a[i] - stock[i]
                        if need > 0:
                            cnt += need * cost[i]
                    return cnt <= budget
                if check(mid):
                    l = mid + 1
                else:
                    r = mid - 1
            return r
    
        return max(f(a) for a in composition)
                            



# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    k: int = deserialize("int", read_line())
    budget: int = deserialize("int", read_line())
    composition: List[List[int]] = deserialize("List[List[int]]", read_line())
    stock: List[int] = deserialize("List[int]", read_line())
    cost: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxNumberOfAlloys(n, k, budget, composition, stock, cost)

    print("\noutput:", serialize(ans))
