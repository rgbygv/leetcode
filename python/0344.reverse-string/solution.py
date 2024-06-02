# Created by Jones at 2024/06/02 12:16
# leetgo: 1.4.7
# https://leetcode.com/problems/reverse-string/

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
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        for i in range(n >> 1):
            s[i], s[n - 1 - i] = s[n - 1 - i], s[i]


# @lc code=end

if __name__ == "__main__":
    s: List[str] = deserialize("List[str]", read_line())
    Solution().reverseString(s)
    ans = s
    print("\noutput:", serialize(ans, "List[str]"))
