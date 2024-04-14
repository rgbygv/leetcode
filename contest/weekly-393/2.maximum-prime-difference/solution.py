# Created by Jones at 2024/04/14 20:40
# leetgo: 1.4.5
# https://leetcode.cn/problems/maximum-prime-difference/
# https://leetcode.cn/contest/weekly-contest-393/problems/maximum-prime-difference/

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

N = 101

p = [True] * N
p[0] = p[1] = False
for i in range(2, N):
    if p[i]:
        for j in range(i + i, N, i):
            p[j] = False


class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        fi = se = -1
        for i, x in enumerate(nums):
            if p[x]:
                if fi == -1:
                    fi = i
                    se = i
                else:
                    se = i
        return se - fi


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maximumPrimeDifference(nums)
    print("\noutput:", serialize(ans, "integer"))
