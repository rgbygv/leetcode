# Created by Jones at 2023/10/24 16:23
# leetgo: dev
# https://leetcode.cn/problems/number-of-dice-rolls-with-target-sum/

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
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        mod = 10**9 + 7

        @cache
        def dfs(n: int, target: int):
            if n == 0:
                return target == 0
            res = sum(dfs(n - 1, target - x) for x in range(1, min(target, k) + 1))

            return res % mod

        return dfs(n, target)


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    k: int = deserialize("int", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().numRollsToTarget(n, k, target)

    print("\noutput:", serialize(ans))
