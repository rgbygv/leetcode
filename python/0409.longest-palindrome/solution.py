# Created by Jones at 2024/06/04 12:15
# leetgo: 1.4.7
# https://leetcode.com/problems/longest-palindrome/

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
    def longestPalindrome(self, s: str) -> int:
        cnt = Counter(s)
        res = 0
        odd = False
        for v in cnt.values():
            if v & 1 == 0:
                res += v
            else:
                odd = True
                res += v - 1
        return res + odd


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().longestPalindrome(s)
    print("\noutput:", serialize(ans, "integer"))
