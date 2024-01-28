# Created by Jones at 2024/01/28 21:18
# leetgo: 1.4.1
# https://leetcode.cn/problems/water-and-jug-problem/

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
    def canMeasureWater(self, a: int, b: int, c: int) -> bool:
        if a > b:
            a, b = b, a
        
        # we can get b - a water, then we can get  a - (b-a)
        
        if c > b + a:
            return False
        
        f = [False] * (a + b + 1)
        f[b] = f[a] = f[a+b] = True

        q = deque([0])
        while q:
            # enumerate we have how many water now
            tn = len(q)
            for _ in range(tn):
                x = q.popleft()
                # if water in a
                if x < a:
                    f[x + b] = True
                    pour = a - x
                    rest = b - pour
                    if not f[rest]:
                        f[rest] = True
                        q.append(rest)
                elif x > a:
                    rest = x - a
                    if not f[rest]:
                        f[rest] = True
                        q.append(rest)
                
                # if water in b
                if x < b:
                    f[x + a] = True
                    pour = b - x
                    if pour < a:
                        rest = a - pour
                        if not f[rest]:
                            f[rest] = True
                            q.append(rest)
        # for i,x in enumerate(f):
        #     print(i, x + 0)
        return f[c]
        
        


# @lc code=end

if __name__ == "__main__":
    jug1Capacity: int = deserialize("int", read_line())
    jug2Capacity: int = deserialize("int", read_line())
    targetCapacity: int = deserialize("int", read_line())
    ans = Solution().canMeasureWater(jug1Capacity, jug2Capacity, targetCapacity)
    print("\noutput:", serialize(ans, "boolean"))
