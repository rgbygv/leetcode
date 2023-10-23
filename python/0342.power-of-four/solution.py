# Created by Jones at 2023/10/23 12:33
# leetgo: dev
# https://leetcode.cn/problems/power-of-four/

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
    def isPowerOfFour(self, n: int) -> bool:
        # pow of 4 must be pow of 2
        if not (n & (n - 1) == 0):
            return False
        return n.bit_length() & 1 == 1


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().isPowerOfFour(n)

    print("\noutput:", serialize(ans))
