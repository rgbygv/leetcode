# Created by Jones at 2024/05/21 14:36
# leetgo: 1.4.7
# https://leetcode.cn/problems/find-the-maximum-achievable-number/

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
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return num + t * 2


# @lc code=end

if __name__ == "__main__":
    num: int = deserialize("int", read_line())
    t: int = deserialize("int", read_line())
    ans = Solution().theMaximumAchievableX(num, t)
    print("\noutput:", serialize(ans, "integer"))
