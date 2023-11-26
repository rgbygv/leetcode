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
        n = len(mat[0])
        k %= n
        if k == 0:
            return True

        for i, row in enumerate(mat):
            if i & 1 == 0:
                tmp = row[k:] + row[:k]
            else:
                tmp = row[-k:] + row[:-k]
            if tmp != row:
                return False

        return True


# @lc code=end

if __name__ == "__main__":
    mat: List[List[int]] = deserialize("List[List[int]]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().areSimilar(mat, k)

    print("\noutput:", serialize(ans))
