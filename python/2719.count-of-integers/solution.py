# Created by Jones at 2024/01/16 15:46
# leetgo: dev
# https://leetcode.cn/problems/count-of-integers/

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
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        @cache
        def dfs(s: str, i: int, is_num: bool, limit: bool, cnt: int):
            if i == len(s):
                return is_num and min_sum <= cnt <= max_sum
            res = 0
            if not is_num:
                res += dfs(s, i + 1, is_num, False, cnt)
            up = 9 if not limit else int(s[i])
            low = 0 if is_num else 1
            for d in range(low, up + 1):
                res += dfs(s, i + 1, True, limit and d == up, cnt + d)
            return res % (int(1e9) + 7)

        return (
            dfs(num2, 0, False, True, 0)
            - dfs(num1, 0, False, True, 0)
            + int(min_sum <= sum(map(int, num1)) <= max_sum)
        ) % (int(1e9) + 7)


# @lc code=end

if __name__ == "__main__":
    num1: str = deserialize("str", read_line())
    num2: str = deserialize("str", read_line())
    min_sum: int = deserialize("int", read_line())
    max_sum: int = deserialize("int", read_line())
    ans = Solution().count(num1, num2, min_sum, max_sum)

    print("\noutput:", serialize(ans))
