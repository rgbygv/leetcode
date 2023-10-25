# Created by Jones at 2023/10/25 09:45
# leetgo: dev
# https://leetcode.cn/problems/find-the-punishment-number-of-an-integer/

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
    def punishmentNumber(self, n: int) -> int:
        def f(x: int):
            xx = x * x
            s = str(xx)
            n = len(s)

            def dfs(i: int, x: int):
                if x < 0:
                    return False
                if i == n:
                    return x == 0

                cur = 0
                for j in range(i, n):
                    cur = cur * 10 + int(s[j])
                    if dfs(j + 1, x - cur):
                        return True
                return False

            if dfs(0, x):
                return xx
            return 0

        return sum(f(x) for x in range(1, n + 1))


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().punishmentNumber(n)

    print("\noutput:", serialize(ans))
