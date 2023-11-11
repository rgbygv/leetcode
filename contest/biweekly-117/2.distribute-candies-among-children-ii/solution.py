# Created by Jones at 2023/11/11 22:30
# leetgo: dev
# https://leetcode.cn/problems/distribute-candies-among-children-ii/
# https://leetcode.cn/contest/biweekly-contest-117/problems/distribute-candies-among-children-ii/

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
    def distributeCandies(self, n: int, limit: int) -> int:
        if n > limit * 3:
            return 0
        if n == limit * 3:
            return 1
        res = 0
        # a < b < c
        for b in range(1, min(n + 1, limit)):
            # c > b
            # 0 <= n - b -c < b
            # c > n-2b
            # c <= limit
            # c <= n -b
            res += 6 * max(min(limit, n - b) - max(b, n - 2 * b), 0)

        # print(res)
        # a == b < c
        for b in range(0, min(n + 1, limit)):
            if b < n - 2 * b <= limit:
                res += 3
        # print(res)

        # a < b == c
        for b in range(0, min(n // 2, limit) + 1):
            # n - 2 * b >= 0
            # b <= n / 2
            if not (n - 2 * b >= 0):
                break
            if n - 2 * b < b:
                res += 3
        # print(res)
        # a == b == c
        if n % 3 == 0:
            res += 1
        return res


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    limit: int = deserialize("int", read_line())
    ans = Solution().distributeCandies(n, limit)

    print("\noutput:", serialize(ans))
