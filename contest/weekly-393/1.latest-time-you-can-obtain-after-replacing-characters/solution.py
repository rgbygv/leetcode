# Created by Jones at 2024/04/14 20:40
# leetgo: 1.4.5
# https://leetcode.cn/problems/latest-time-you-can-obtain-after-replacing-characters/
# https://leetcode.cn/contest/weekly-contest-393/problems/latest-time-you-can-obtain-after-replacing-characters/

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
    def findLatestTime(self, s: str) -> str:
        h, m = s.split(":")
        if h == "??":
            h = "11"
        elif h[0] == "?":
            if h[1] >= "2":
                h = "0" + h[1]
            else:
                h = "1" + h[1]
        elif h[1] == "?":
            if h[0] == "0":
                h = h[0] + "9"
            else:
                h = h[0] + "1"
        if m == "??":
            m = "59"
        elif m[0] == "?":
            m = "5" + m[1]
        elif m[1] == "?":
            m = m[0] + "9"
        return h + ":" + m


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().findLatestTime(s)
    print("\noutput:", serialize(ans, "string"))
