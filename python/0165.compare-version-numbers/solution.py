# Created by Jones at 2024/05/03 13:32
# leetgo: 1.4.5
# https://leetcode.com/problems/compare-version-numbers/

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
    def compareVersion(self, version1: str, version2: str) -> int:
        s1 = version1.split(".")
        s2 = version2.split(".")
        for x, y in zip_longest(s1, s2, fillvalue="0"):
            x, y = int(x), int(y)
            if x > y:
                return 1
            if x < y:
                return -1
        return 0


# @lc code=end

if __name__ == "__main__":
    version1: str = deserialize("str", read_line())
    version2: str = deserialize("str", read_line())
    ans = Solution().compareVersion(version1, version2)
    print("\noutput:", serialize(ans, "integer"))
