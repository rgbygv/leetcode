# Created by Jones at 2024/06/01 12:39
# leetgo: 1.4.7
# https://leetcode.cn/problems/distribute-candies-among-children-i/

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
    def distributeCandies(self, n: int, limit: int) -> int:
        """
        - `1 <= n <= 50`
        - `1 <= limit <= 50`
        """

        @cache
        def dfs(i: int, x: int):
            """
            divide `x` candy to `i` child
            """
            if i == 0:
                return int(x == 0)
            res = 0
            for y in range( min(x, limit) + 1):
                res += dfs(i - 1, x - y)
            return res

        return dfs(3, n)


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    limit: int = deserialize("int", read_line())
    ans = Solution().distributeCandies(n, limit)
    print("\noutput:", serialize(ans, "integer"))
