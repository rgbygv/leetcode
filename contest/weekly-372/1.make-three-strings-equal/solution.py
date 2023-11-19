# Created by Jones at 2023/11/19 10:30
# leetgo: dev
# https://leetcode.cn/problems/make-three-strings-equal/
# https://leetcode.cn/contest/weekly-contest-372/problems/make-three-strings-equal/

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
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        n = len(s1) + len(s2) + len(s3)

        res = inf

        for i in range(len(s1)):
            if s1[: i + 1] == s2[: i + 1] == s3[: i + 1]:
                res = min(res, n - 3 * (i + 1))
        if res == inf:
            return -1

        return res


# @lc code=end

if __name__ == "__main__":
    s1: str = deserialize("str", read_line())
    s2: str = deserialize("str", read_line())
    s3: str = deserialize("str", read_line())
    ans = Solution().findMinimumOperations(s1, s2, s3)

    print("\noutput:", serialize(ans))
