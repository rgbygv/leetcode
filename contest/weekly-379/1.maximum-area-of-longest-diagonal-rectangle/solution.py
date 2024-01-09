# Created by Jones at 2024/01/09 20:52
# leetgo: dev
# https://leetcode.cn/problems/maximum-area-of-longest-diagonal-rectangle/
# https://leetcode.cn/contest/weekly-contest-379/problems/maximum-area-of-longest-diagonal-rectangle/

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
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        res = 0
        mx = 0
        for x, y in dimensions:
            cur = x * x + y * y
            if cur > mx or cur == mx and x * y > res:
                res = x * y
                mx = cur
        return res


# @lc code=end

if __name__ == "__main__":
    dimensions: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().areaOfMaxDiagonal(dimensions)

    print("\noutput:", serialize(ans))
