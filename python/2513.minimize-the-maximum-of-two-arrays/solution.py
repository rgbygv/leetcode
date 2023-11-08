# Created by Jones at 2023/11/08 19:28
# leetgo: dev
# https://leetcode.cn/problems/minimize-the-maximum-of-two-arrays/

from typing import *
from leetgo_py import *

from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from copy import deepcopy
from functools import cache, cmp_to_key, lru_cache, reduce
from heapq import heapify, heappop, heappush, heappushpop, heapreplace
from itertools import accumulate, chain, count, pairwise, zip_longest
from math import ceil, comb, floor, gcd, inf, isqrt, log2, perm, sqrt, lcm
from operator import xor
from string import ascii_lowercase
from typing import List, Optional

# @lc code=begin
# from sortedcontainers import SortedList


class Solution:
    def minimizeSet(
        self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int
    ) -> int:
        if divisor1 > divisor2:
            divisor1, divisor2 = divisor2, divisor1
            uniqueCnt1, uniqueCnt2 = uniqueCnt2, uniqueCnt1
        l = 0
        # r = 2 * 10**9
        r = (uniqueCnt1 + uniqueCnt2) * 2  # Wrong case: d1 = d2 = 2
        while l < r:
            mid = (l + r) >> 1
            a = mid // divisor1
            b = mid // divisor2
            c = mid // (lcm(divisor1, divisor2))
            # print(mid, a, b, c)
            if (
                mid - a >= uniqueCnt1
                and mid - b >= uniqueCnt2
                and mid - c >= uniqueCnt1 + uniqueCnt2
            ):
                r = mid
            else:
                l = mid + 1
        return l


# @lc code=end

if __name__ == "__main__":
    divisor1: int = deserialize("int", read_line())
    divisor2: int = deserialize("int", read_line())
    uniqueCnt1: int = deserialize("int", read_line())
    uniqueCnt2: int = deserialize("int", read_line())
    ans = Solution().minimizeSet(divisor1, divisor2, uniqueCnt1, uniqueCnt2)

    print("\noutput:", serialize(ans))
