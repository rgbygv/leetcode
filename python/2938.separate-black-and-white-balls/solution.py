# Created by Jones at 2024/06/06 08:32
# leetgo: 1.4.7
# https://leetcode.cn/problems/separate-black-and-white-balls/

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
    def minimumSteps(self, s: str) -> int:
        res = 0
        black = 0
        for ch in s:
            if ch == "0":
                res += black
            else:
                black += 1
        return res


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().minimumSteps(s)
    print("\noutput:", serialize(ans, "long"))
