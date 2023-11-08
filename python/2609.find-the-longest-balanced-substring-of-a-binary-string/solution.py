# Created by Jones at 2023/11/08 14:00
# leetgo: dev
# https://leetcode.cn/problems/find-the-longest-balanced-substring-of-a-binary-string/

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
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        res = 0

        zero = one = 0
        for ch in s:
            if ch == "0":
                if one != 0:
                    zero = 0
                zero += 1
                one = 0
            else:
                one += 1
                res = max(res, min(one, zero))

        return res * 2


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().findTheLongestBalancedSubstring(s)

    print("\noutput:", serialize(ans))
