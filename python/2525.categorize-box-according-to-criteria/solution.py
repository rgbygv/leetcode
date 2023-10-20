# Created by Jones at 2023/10/20 13:41
# leetgo: dev
# https://leetcode.cn/problems/categorize-box-according-to-criteria/

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
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        bulky = (
            max(length, width, height) >= 10**4 or length * width * height >= 10**9
        )
        heavy = mass >= 100

        if bulky and heavy:
            return "Both"
        if not bulky and not heavy:
            return "Neither"
        return "Bulky" if bulky else "Heavy"


# @lc code=end

if __name__ == "__main__":
    length: int = deserialize("int", read_line())
    width: int = deserialize("int", read_line())
    height: int = deserialize("int", read_line())
    mass: int = deserialize("int", read_line())
    ans = Solution().categorizeBox(length, width, height, mass)

    print("\noutput:", serialize(ans))
