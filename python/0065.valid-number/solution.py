# Created by Jones at 2024/03/10 21:56
# leetgo: 1.4.1
# https://leetcode.cn/problems/valid-number/

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
from pprint import pprint
from string import ascii_lowercase
from typing import List, Optional

# @lc code=begin

class Solution:
    def isNumber(self, s: str) -> bool:
        op = False # + -

        n = len(s)

        def is_num(s):
            return not s or all(ch.isdigit() for ch in s)

        def is_int(s:str) -> bool:
            if not s:
                return False
            if s[0] in "+-":
                s = s[1:]
            return bool(s) and is_num(s)
        
        def is_float(s:str) -> bool:
            if "." not in s:
                return False
            if s[0] in "+-":
                s = s[1:]
            a = s.split(".")
            if len(a) > 2:
                return False
            pre, suf = a
            if not pre and not suf:
                return False
            return is_num(pre) and is_num(suf)
        if "e" in s or "E" in s:
            a = s.lower().split("e")
            if len(a) != 2:
                return False
            pre, suf = a
            return (is_int(pre) or is_float(pre)) and is_int(suf)
        return is_int(s) or is_float(s) 

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().isNumber(s)
    print("\noutput:", serialize(ans, "boolean"))
