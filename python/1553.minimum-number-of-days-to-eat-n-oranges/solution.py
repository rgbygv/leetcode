# Created by Jones at 2024/05/12 11:03
# leetgo: 1.4.7
# https://leetcode.cn/problems/minimum-number-of-days-to-eat-n-oranges/

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
    def minDays(self, n: int) -> int:
        @cache
        def dfs(n: int):
            if n == 1:
                return 1
            if n <= 3:
                return 2
            # mod 2
            op1 = (n & 1) + 1 + dfs(n // 2)
            # mod 3
            op2 = (n % 3) + 1 + dfs(n // 3)
            return min(op1, op2)

        return dfs(n)


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().minDays(n)
    print("\noutput:", serialize(ans, "integer"))
