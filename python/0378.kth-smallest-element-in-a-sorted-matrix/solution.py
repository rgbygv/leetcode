# Created by Jones at 2024/03/16 15:23
# leetgo: 1.4.2
# https://leetcode.cn/problems/kth-smallest-element-in-a-sorted-matrix/

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
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        l = matrix[0][0]
        r = matrix[n - 1][n - 1]

        while l < r:
            mid = (l + r) >> 1

            # find how many number <= mid
            def check(mid):
                j = bisect_right(matrix[0], mid) - 1
                res = j + 1
                for i in range(1, n):
                    while j >= 0 and matrix[i][j] > mid:
                        j -= 1
                    if j == -1:
                        break
                    res += j + 1
                return res >= k

            if not check(mid):
                l = mid + 1
            else:
                r = mid
        return l


# @lc code=end

if __name__ == "__main__":
    matrix: List[List[int]] = deserialize("List[List[int]]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().kthSmallest(matrix, k)
    print("\noutput:", serialize(ans, "integer"))
