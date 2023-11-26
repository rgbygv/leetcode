# Created by Jones at 2023/11/26 10:30
# leetgo: dev
# https://leetcode.cn/problems/matrix-similarity-after-cyclic-shifts/
# https://leetcode.cn/contest/weekly-contest-373/problems/matrix-similarity-after-cyclic-shifts/

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
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m = len(mat)
        n = len(mat[0])

        res = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i & 1:
                    res[i][(j + k) % n] = mat[i][j]
                else:
                    # print(i, (j - k) % n)
                    res[i][(j - k) % n] = mat[i][j]
            # print(res[i])
            if res[i] != mat[i]:
                return False
        return True


# @lc code=end

if __name__ == "__main__":
    mat: List[List[int]] = deserialize("List[List[int]]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().areSimilar(mat, k)

    print("\noutput:", serialize(ans))
