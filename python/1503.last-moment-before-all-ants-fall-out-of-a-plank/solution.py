# Created by Jones at 2023/11/04 14:33
# leetgo: dev
# https://leetcode.cn/problems/last-moment-before-all-ants-fall-out-of-a-plank/

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
# from sortedcontainers import SortedList


class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        res = 0
        if left:
            res = max(left)
        if right:
            res = max(res, n - min(right))
        return res


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    left: List[int] = deserialize("List[int]", read_line())
    right: List[int] = deserialize("List[int]", read_line())
    ans = Solution().getLastMoment(n, left, right)

    print("\noutput:", serialize(ans))
