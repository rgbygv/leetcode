# Created by Jones at 2024/05/05 16:09
# leetgo: 1.4.6
# https://leetcode.cn/problems/ugly-number-iii/

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
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        """
        - `1 <= n, a, b, c <= 10⁹`
        - `1 <= a * b * c <= 10¹⁸`
        - It is guaranteed that the result will be in range `[1, 2 * 10⁹]`.
        """

        l, r = 1, 2 * 10**9 + 1
        while l < r:
            mid = (l + r) >> 1

            def check(mid):
                cnt = (
                    mid // a
                    + mid // b
                    + mid // c
                    - mid // lcm(a, b)
                    - mid // lcm(a, c)
                    - mid // lcm(b, c)
                    + mid // lcm(a, b, c)
                )
                return cnt >= n

            if check(mid):
                r = mid
            else:
                l = mid + 1
        return l


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    a: int = deserialize("int", read_line())
    b: int = deserialize("int", read_line())
    c: int = deserialize("int", read_line())
    ans = Solution().nthUglyNumber(n, a, b, c)
    print("\noutput:", serialize(ans, "integer"))
