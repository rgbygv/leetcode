# Created by Jones at 2024/04/13 12:34
# leetgo: 1.4.5
# https://leetcode.com/problems/maximal-rectangle/

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
from pprint import pprint
from string import ascii_lowercase
from typing import List, Optional

# @lc code=begin


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def calc_row(row: list[int]):
            # O(n * n), use `DP` or `Mono Stack` can be optimized to O(n)
            n = len(row)
            res = 0
            for j, x in enumerate(row):
                if x == 0:
                    continue
                i = j - 1
                while i >= 0 and row[i] >= x:
                    i -= 1
                k = j + 1
                while k < n and row[k] >= x:
                    k += 1
                res = max(res, (k - 1 - i) * x)
            # print(row, res)
            return res

        res = 0

        n = len(matrix[0])
        row = [0] * n
        # O(m * n)
        for cur in matrix:
            for j, x in enumerate(cur):
                if x == "0":
                    row[j] = 0
                else:
                    row[j] += 1
            res = max(res, calc_row(row))
        return res


# @lc code=end

if __name__ == "__main__":
    matrix: List[List[str]] = deserialize("List[List[str]]", read_line())
    ans = Solution().maximalRectangle(matrix)
    print("\noutput:", serialize(ans, "integer"))
