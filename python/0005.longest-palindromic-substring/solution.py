# Created by Jones at 2023/10/27 21:26
# leetgo: dev
# https://leetcode.cn/problems/longest-palindromic-substring/

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
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        def check(i, j):
            while i >= 0 and j < n and s[i] == s[j]:
                i -= 1
                j += 1

            return j - i - 1

        max_len = 0
        idx = 0, 0
        for i in range(n):
            if (cur := check(i, i)) > max_len:
                max_len = cur
                idx = i, i
            if (cur := check(i, i + 1)) > max_len:
                max_len = cur
                idx = i, i + 1

        i, j = idx
        half = max_len >> 1
        if i == j:
            return s[i - half : i + half + 1]
        return s[i + 1 - half : j + half]


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().longestPalindrome(s)

    print("\noutput:", serialize(ans))
