# Created by Jones at 2023/10/31 19:30
# leetgo: dev
# https://leetcode.cn/problems/find-the-original-array-of-prefix-xor/

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
    def findArray(self, pref: List[int]) -> List[int]:
        res = [0] * len(pref)

        for i, x in enumerate(pref):
            if i == 0:
                res[i] = x
            else:
                res[i] = x ^ pref[i - 1]

        return res


# @lc code=end

if __name__ == "__main__":
    pref: List[int] = deserialize("List[int]", read_line())
    ans = Solution().findArray(pref)

    print("\noutput:", serialize(ans))
