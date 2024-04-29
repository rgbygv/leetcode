# Created by Jones at 2024/04/29 15:06
# leetgo: 1.4.5
# https://leetcode.cn/problems/bitwise-ors-of-subarrays/

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
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        ans = set()
        cur = set()
        for x in arr:
            cur = {y | x for y in cur} | {x}
            ans |= cur
        return len(ans)


# class Solution:
#     def subarrayBitwiseORs(self, arr: List[int]) -> int:
#         N = 31
#         # what the most res is?

#         # if now we are 11011, the only one can make res diff is
#         # have diffrent ones, so each turn at most have 31 answer

#         appear = [[] for _ in range(N)]  # the bits appear
#         for i, x in enumerate(arr):
#             for d in range(N):
#                 if x >> d & 1:
#                     appear[d].append(i)

#         # can we store all the answer?
#         seen = set()
#         for i, x in enumerate(arr):
#             res = x
#             seen.add(res)
#             # find the bit can use
#             can = set(d for d, v in enumerate(appear) if v)
#             for d in range(N):
#                 if x >> d & 1:
#                     can.remove(d)
#             # print(res, can, appear[:5])
#             while can:
#                 # we should find the minimal j have 1 res don't have
#                 j = inf
#                 for d in can:
#                     v = appear[d]
#                     k = bisect_left(v, i)
#                     if k != len(v):
#                         j = min(j, v[k])
#                 if j == inf:
#                     break
#                 for d in can.copy():
#                     if arr[j] >> d & 1:
#                         can.remove(d)
#                 res |= arr[j]
#                 seen.add(res)
#         # print([bin(x) for x in seen])
#         return len(seen)


# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    ans = Solution().subarrayBitwiseORs(arr)
    print("\noutput:", serialize(ans, "integer"))
