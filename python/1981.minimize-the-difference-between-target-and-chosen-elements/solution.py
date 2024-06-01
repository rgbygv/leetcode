# Created by Jones at 2024/06/01 12:55
# leetgo: 1.4.7
# https://leetcode.cn/problems/minimize-the-difference-between-target-and-chosen-elements/

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
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        """
        - `m == mat.length`
        - `n == mat[i].length`
        - `1 <= m, n <= 70`
        - `1 <= mat[i][j] <= 70`
        - `1 <= target <= 800`
        """
        m = len(mat)
        f = set(mat[0])
        for i in range(1, m):
            g = set()
            for x in f:
                for y in mat[i]:
                    g.add(x + y)
            f = g
        return min(abs(x - target) for x in f)


# @lc code=end

if __name__ == "__main__":
    mat: List[List[int]] = deserialize("List[List[int]]", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().minimizeTheDifference(mat, target)
    print("\noutput:", serialize(ans, "integer"))
