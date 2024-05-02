# Created by Jones at 2024/05/02 19:30
# leetgo: 1.4.5
# https://leetcode.cn/problems/minimum-score-triangulation-of-polygon/

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
    def minScoreTriangulation(self, a: List[int]) -> int:
        # n is really small

        @cache
        def dfs(l: int, r: int):
            if r - l <= 2:
                if r - l < 2:
                    return 0
                return reduce(lambda x, y: x * y, a[l : r + 1])
            # enumerate mid
            tmp = a[l] * a[r]
            return min(
                (tmp * a[mid] + dfs(l, mid) + dfs(mid, r)) for mid in range(l + 1, r)
            )
            # ic(l, r, res)

        return dfs(0, len(a) - 1)


# @lc code=end

if __name__ == "__main__":
    values: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minScoreTriangulation(values)
    print("\noutput:", serialize(ans, "integer"))
