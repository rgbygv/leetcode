# Created by Jones at 2024/01/08 20:07
# leetgo: dev
# https://leetcode.cn/problems/number-of-boomerangs/

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
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        n = len(points)

        def calc(i, j):
            return (points[i][0] - points[j][0]) ** 2 + (
                points[i][1] - points[j][1]
            ) ** 2

        res = 0
        for i in range(n):
            cnt = Counter()
            for j in range(n):
                cnt[calc(i, j)] += 1
            for v in cnt.values():
                res += (v) * (v - 1)

        return res


# @lc code=end

if __name__ == "__main__":
    points: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().numberOfBoomerangs(points)

    print("\noutput:", serialize(ans))
