# Created by Jones at 2023/11/11 22:30
# leetgo: dev
# https://leetcode.cn/problems/number-of-strings-which-can-be-rearranged-to-contain-substring/
# https://leetcode.cn/contest/biweekly-contest-117/problems/number-of-strings-which-can-be-rearranged-to-contain-substring/

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
    def stringCount(self, n: int) -> int:
        mod = 10**9 + 7
        if n < 3:
            return 0
        # must have leet
        # other's any
        # res = 12
        # for i in range(5, n + 1):
        #     res = res * i * 26 % mod
        # return res
        # aabb

        # why not cant leet

        res = pow(26, n, mod)
        less_l = less_t = pow(25, n, mod)
        less_lt = pow(24, n, mod)
        less_le = less_te = pow(24, n, mod) + n * pow(24, n - 1, mod)
        less_lte = pow(23, n, mod) + n * pow(23, n - 1, mod)
        less_e = less_l + n * pow(25, n - 1, mod)
        return (
            res - less_l - less_t - less_e + less_lt + less_le + less_te - less_lte
        ) % mod


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().stringCount(n)

    print("\noutput:", serialize(ans))
