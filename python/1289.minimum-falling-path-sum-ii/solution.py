# Created by Jones at 2024/04/26 13:30
# leetgo: 1.4.5
# https://leetcode.com/problems/minimum-falling-path-sum-ii/

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
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        pre = grid[0]

        for i in range(1, m):
            cur = [0] * n
            # we can enumerate the pre and find (min(pre[j]) where j != i) but it's not effcient
            # we can use a heap to reduce the process of find min
            # actually we only need the 2 smallest pre
            smallest = sorted(zip(pre, range(n)))[:2]
            # print(pre, smallest)
            for j, x in enumerate(grid[i]):
                if j == smallest[0][1]:
                    cur[j] = x + smallest[1][0]
                else:
                    cur[j] = x + smallest[0][0]
            pre = cur
        # print(pre)
        return min(pre)


# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().minFallingPathSum(grid)
    print("\noutput:", serialize(ans, "integer"))
