# Created by Jones at 2023/12/13 15:51
# leetgo: dev
# https://leetcode.cn/problems/lexicographically-smallest-palindrome/

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
    def makeSmallestPalindrome(self, s: str) -> str:
        n = len(s)
        left = []
        for i in range(n >> 1):
            if s[i] != s[n - 1 - i]:
                left.append(min(s[i], s[n - 1 - i]))
            else:
                left.append(s[i])
        tmp = "".join(left)
        if n & 1:
            return tmp + s[n >> 1] + tmp[::-1]
        return tmp + tmp[::-1]


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().makeSmallestPalindrome(s)

    print("\noutput:", serialize(ans))
