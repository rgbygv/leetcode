# Created by Jones at 2024/01/06 22:30
# leetgo: dev
# https://leetcode.cn/problems/count-the-number-of-powerful-integers/
# https://leetcode.cn/contest/biweekly-contest-121/problems/count-the-number-of-powerful-integers/

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
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        n = len(s)

        @cache
        def dfs(num: str, i: int, is_num: bool, is_limit: bool):
            m = len(num)
            if m < n:
                return 0
            if i >= m:
                return 1

            if i + n >= m:
                d = int(s[i + n - m])  # this must be same
                if is_limit and d > int(num[i]):
                    return 0
                return dfs(num, i + 1, is_num, is_limit and d == int(num[i]))

            res = 0
            if not is_num:
                res = dfs(num, i + 1, is_num, False)

            low = 0 if is_num else 1
            up = 9 if not is_limit else int(num[i])
            for d in range(low, min(up, limit) + 1):
                res += dfs(num, i + 1, True, is_limit and d == up)

            return res

        return dfs(str(finish), 0, False, True) - dfs(str(start - 1), 0, False, True)


# @lc code=end

if __name__ == "__main__":
    start: int = deserialize("int", read_line())
    finish: int = deserialize("int", read_line())
    limit: int = deserialize("int", read_line())
    s: str = deserialize("str", read_line())
    ans = Solution().numberOfPowerfulInt(start, finish, limit, s)

    print("\noutput:", serialize(ans))
