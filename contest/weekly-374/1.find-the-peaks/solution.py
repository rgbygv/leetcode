# Created by Jones at 2023/12/03 10:30
# leetgo: dev
# https://leetcode.cn/problems/find-the-peaks/
# https://leetcode.cn/contest/weekly-contest-374/problems/find-the-peaks/

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
    def findPeaks(self, mountain: List[int]) -> List[int]:
        n = len(mountain)
        return [
            i
            for i in range(1, n - 1)
            if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]
        ]


# @lc code=end

if __name__ == "__main__":
    mountain: List[int] = deserialize("List[int]", read_line())
    ans = Solution().findPeaks(mountain)

    print("\noutput:", serialize(ans))
