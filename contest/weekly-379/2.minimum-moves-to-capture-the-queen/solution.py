# Created by Jones at 2024/01/09 20:52
# leetgo: dev
# https://leetcode.cn/problems/minimum-moves-to-capture-the-queen/
# https://leetcode.cn/contest/weekly-contest-379/problems/minimum-moves-to-capture-the-queen/

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


class Solution:
    def minMovesToCaptureTheQueen(
        self, a: int, b: int, c: int, d: int, e: int, f: int
    ) -> int:
        # ans <= 2
        if a == e and (a != c or not (b < d < f or f < d < b)):
            return 1
        if b == f and (b != d or not (a < c < e or e < c < a)):
            return 1

        if c - d == e - f and not (a - b == c - d and ((c < a < e) or (e < a < c))):
            return 1

        if c + d == e + f and not (a + b == c + d and ((c < a < e) or (e < a < c))):
            return 1

        return 2


# @lc code=end

if __name__ == "__main__":
    a: int = deserialize("int", read_line())
    b: int = deserialize("int", read_line())
    c: int = deserialize("int", read_line())
    d: int = deserialize("int", read_line())
    e: int = deserialize("int", read_line())
    f: int = deserialize("int", read_line())
    ans = Solution().minMovesToCaptureTheQueen(a, b, c, d, e, f)

    print("\noutput:", serialize(ans))
