# Created by Jones at 2023/11/11 22:30
# leetgo: dev
# https://leetcode.cn/problems/distribute-candies-among-children-i/
# https://leetcode.cn/contest/biweekly-contest-117/problems/distribute-candies-among-children-i/

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
        res = 0
        k = min(limit, n) + 1
        for a in range(k):
            for b in range(k):
                for c in range(k):
                    if a + b + c == n:
                        res += 1
        return res


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    limit: int = deserialize("int", read_line())
    ans = Solution().distributeCandies(n, limit)

    print("\noutput:", serialize(ans))
