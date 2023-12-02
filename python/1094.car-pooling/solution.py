# Created by Jones at 2023/12/02 12:16
# leetgo: dev
# https://leetcode.cn/problems/car-pooling/

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
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda e: e[1])
        N = 1001
        diff = [0] * N
        d = 0

        j = 0
        n = len(trips)
        for i in range(0, N):
            while j < n and trips[j][1] <= i:
                num, start, end = trips[j]
                diff[start] += num
                diff[end] -= num
                j += 1
            d += diff[i]
            if d > capacity:
                return False
            if j == n:
                break

        return True


# @lc code=end

if __name__ == "__main__":
    trips: List[List[int]] = deserialize("List[List[int]]", read_line())
    capacity: int = deserialize("int", read_line())
    ans = Solution().carPooling(trips, capacity)

    print("\noutput:", serialize(ans))
