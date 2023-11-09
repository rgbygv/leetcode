# Created by Jones at 2023/11/09 14:24
# leetgo: dev
# https://leetcode.cn/problems/count-number-of-homogenous-substrings/

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
    def countHomogenous(self, s: str) -> int:
        mod = 10**9 + 7
        pre = 0
        cnt = 0
        res = 0
        for ch in s:
            if ch == pre:
                cnt += 1
            else:
                pre = ch
                cnt = 1
            res += cnt
        return res % mod


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().countHomogenous(s)

    print("\noutput:", serialize(ans))
