# Created by Jones at 2024/02/25 19:31
# leetgo: 1.4.1
# https://leetcode.cn/problems/find-the-largest-area-of-square-inside-two-rectangles/
# https://leetcode.cn/contest/weekly-contest-386/problems/find-the-largest-area-of-square-inside-two-rectangles/

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
    def largestSquareArea(
        self, bottomLeft: List[List[int]], topRight: List[List[int]]
    ) -> int:
        res = 0
        n = len(bottomLeft)
        for i in range(n):
            b1 = bottomLeft[i]
            t1 = topRight[i]
            for j in range(i):
                b2 = bottomLeft[j]
                t2 = topRight[j]
                height = min(t1[1], t2[1]) - max(b1[1], b2[1])
                width = min(t1[0], t2[0]) - max(b1[0], b2[0])
                size = min(height, width)
                if size > 0:
                    res = max(res, size)
        return res * res


# @lc code=end

if __name__ == "__main__":
    bottomLeft: List[List[int]] = deserialize("List[List[int]]", read_line())
    topRight: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().largestSquareArea(bottomLeft, topRight)
    print("\noutput:", serialize(ans, "long"))
