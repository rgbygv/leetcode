# Created by Jones at 2024/06/03 10:24
# leetgo: 1.4.7
# https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/

from typing import *
from leetgo_py import *

from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from functools import cache, cmp_to_key, lru_cache, reduce
from heapq import heapify, heappop, heappush, heappushpop, heapreplace
from icecream import ic
from itertools import accumulate, chain, count, pairwise, zip_longest
from math import ceil, comb, floor, gcd, inf, isqrt, lcm, log2, perm, sqrt
from operator import xor
from pprint import pprint
from string import ascii_lowercase
from typing import List, Optional

# @lc code=begin


class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        i = j = 0
        while i < m and j < n:
            while i < m and s[i] != t[j]:
                i += 1
            if i < m:
                i += 1
                j += 1
        return n - j


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    t: str = deserialize("str", read_line())
    ans = Solution().appendCharacters(s, t)
    print("\noutput:", serialize(ans, "integer"))
