# Created by Jones at 2023/11/11 22:30
# leetgo: dev
# https://leetcode.cn/problems/maximum-spending-after-buying-items/
# https://leetcode.cn/contest/biweekly-contest-117/problems/maximum-spending-after-buying-items/

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
# from sortedcontainers import SortedList


class Solution:
    def maxSpending(self, values: List[List[int]]) -> int:
        m = len(values)
        n = len(values[0])

        q = []
        for i in range(m):
            heappush(q, (values[i][-1], i))

        res = 0
        for j in range(1, m * n + 1):
            x, i = heappop(q)
            res += x * j
            values[i].pop()
            if values[i]:
                heappush(q, (values[i][-1], i))
        return res


# @lc code=end

if __name__ == "__main__":
    values: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().maxSpending(values)

    print("\noutput:", serialize(ans))
