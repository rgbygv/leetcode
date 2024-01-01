# Created by Bob at 2024/01/01 21:36
# leetgo: dev
# https://leetcode.cn/problems/maximum-profit-of-operating-a-centennial-wheel/

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
    def minOperationsMaxProfit(
        self, customers: List[int], boardingCost: int, runningCost: int
    ) -> int:
        if boardingCost * 4 <= runningCost:
            return -1

        cnt = 0
        res = -1
        i = 1
        n = len(customers)
        while i <= n or cnt > 0:
            if i <= n:
                cnt += customers[i - 1]
            cur = min(cnt, 4)
            # print(i, cnt, cur)
            cnt -= cur
            score = cur * boardingCost - runningCost
            if score > 0:
                res = i
            i += 1
        return res


# @lc code=end

if __name__ == "__main__":
    customers: List[int] = deserialize("List[int]", read_line())
    boardingCost: int = deserialize("int", read_line())
    runningCost: int = deserialize("int", read_line())
    ans = Solution().minOperationsMaxProfit(customers, boardingCost, runningCost)

    print("\noutput:", serialize(ans))
