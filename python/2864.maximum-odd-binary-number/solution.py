# Created by Jones at 2024/03/13 13:01
# leetgo: 1.4.2
# https://leetcode.cn/problems/maximum-odd-binary-number/

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
    def maximumOddBinaryNumber(self, s: str) -> str:
        cnt = s.count("1")
        return "1" * (cnt - 1) + "0" * (len(s) - cnt) + "1"


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().maximumOddBinaryNumber(s)
    print("\noutput:", serialize(ans, "string"))
