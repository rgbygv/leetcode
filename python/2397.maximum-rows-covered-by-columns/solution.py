# Created by Bob at 2024/01/04 21:50
# leetgo: dev
# https://leetcode.cn/problems/maximum-rows-covered-by-columns/

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
    def maximumRows(self, a: List[List[int]], numSelect: int) -> int:
        m = len(a)
        n = len(a[0])

        res = 0
        for mask in range(1 << n):
            cur = mask.bit_count()
            if cur != numSelect:
                continue

            cur_res = 0

            for i in range(m):
                ok = True
                for j in range(n):
                    if a[i][j] == 1:
                        ok = ok and (mask >> j & 1)
                cur_res += ok
            res = max(res, cur_res)
        return res


# @lc code=end

if __name__ == "__main__":
    matrix: List[List[int]] = deserialize("List[List[int]]", read_line())
    numSelect: int = deserialize("int", read_line())
    ans = Solution().maximumRows(matrix, numSelect)

    print("\noutput:", serialize(ans))
