# Created by Jones at 2024/05/26 14:04
# leetgo: 1.4.7
# https://leetcode.cn/problems/find-kth-largest-xor-coordinate-value/

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
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        """
        - `m == matrix.length`
        - `n == matrix[i].length`
        - `1 <= m, n <= 1000`
        - `0 <= matrix[i][j] <= 10⁶`
        - `1 <= k <= m * n`
        """
        q = []
        m, n = len(matrix), len(matrix[0])
        f = [[0] * (n + 1) for _ in range(m + 1)]

        for i, row in enumerate(matrix, 1):
            for j, x in enumerate(row, 1):
                f[i][j] = x ^ f[i - 1][j] ^ f[i][j - 1] ^ f[i - 1][j - 1]
                q.append(f[i][j])
        return sorted(q, reverse=True)[k - 1]


# @lc code=end

if __name__ == "__main__":
    matrix: List[List[int]] = deserialize("List[List[int]]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().kthLargestValue(matrix, k)
    print("\noutput:", serialize(ans, "integer"))
