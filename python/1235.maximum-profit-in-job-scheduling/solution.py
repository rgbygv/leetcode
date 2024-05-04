# Created by Jones at 2024/05/04 12:33
# leetgo: 1.4.5
# https://leetcode.cn/problems/maximum-profit-in-job-scheduling/

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
    def jobScheduling(
        self, startTime: List[int], endTime: List[int], profit: List[int]
    ) -> int:
        # - `1 <= startTime.length == endTime.length == profit.length <= 5 * 10⁴`
        # - `1 <= startTime[i] < endTime[i] <= 10⁹`
        # - `1 <= profit[i] <= 10⁴`
        q = sorted(zip(startTime, endTime, profit))
        n = len(q)

        @cache
        def dfs(i: int):
            if i == n:
                return 0
            # choose q[i]
            start, end, score = q[i]
            j = bisect_left(q, end, key=lambda e: e[0])
            op1 = score + dfs(j)
            # don't choose
            op2 = dfs(i + 1)
            return max(op1, op2)

        return dfs(0)


# @lc code=end

if __name__ == "__main__":
    startTime: List[int] = deserialize("List[int]", read_line())
    endTime: List[int] = deserialize("List[int]", read_line())
    profit: List[int] = deserialize("List[int]", read_line())
    ans = Solution().jobScheduling(startTime, endTime, profit)
    print("\noutput:", serialize(ans, "integer"))
