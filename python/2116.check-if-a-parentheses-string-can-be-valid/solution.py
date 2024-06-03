# Created by Jones at 2024/06/03 10:27
# leetgo: 1.4.7
# https://leetcode.cn/problems/check-if-a-parentheses-string-can-be-valid/

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
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) & 1:
            return False

        # memo limit
        # n = len(s)
        # @cache
        # def dfs(i: int, cnt):
        #     if cnt < 0:
        #         return False
        #     if i == n:
        #         return cnt == 0
        #     if locked[i] == "0":
        #         return dfs(i + 1, cnt + 1) or dfs(i + 1, cnt - 1)
        #     return dfs(i + 1, cnt + (1 if s[i] == "(" else -1))

        # return dfs(0, 0)

        mn = mx = 0
        for i, (ch, lock) in enumerate(zip(s, locked)):
            if lock == "0":
                mx = mx + 1
                mn = max(mn - 1, (i + 1) & 1)
            else:
                diff = 1 if ch == "(" else -1
                mx += diff
                mn = max(mn + diff, (i + 1) & 1)
            # ic(ch, lock, mx, mn)
            if mx < mn:
                return False
        # ic(mx, mn)
        return mn == 0


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    locked: str = deserialize("str", read_line())
    ans = Solution().canBeValid(s, locked)
    print("\noutput:", serialize(ans, "boolean"))
