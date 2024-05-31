# Created by Jones at 2024/05/31 10:21
# leetgo: 1.4.7
# https://leetcode.cn/problems/maximum-number-of-points-with-cost/

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
    def maxPoints(self, points: List[List[int]]) -> int:
        m = len(points)
        n = len(points[0])

        f = points[0]
        for idx in range(1, m):
            left = [0] * n
            for i, x in enumerate(f):
                left[i] = x - (n - i)
                if i > 0 and left[i] < left[i - 1]:
                    left[i] = left[i - 1]
            right = [0] * n
            for i in range(n - 1, -1, -1):
                right[i] = f[i] - i
                if i < n - 1 and right[i] < right[i + 1]:
                    right[i] = right[i + 1]

            g = [0] * n
            for j, x in enumerate(points[idx]):
                g[j] = x + max(left[j] + n - j, right[j] + j)
            f = g
        return max(f)


# @lc code=end

if __name__ == "__main__":
    points: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().maxPoints(points)
    print("\noutput:", serialize(ans, "long"))
