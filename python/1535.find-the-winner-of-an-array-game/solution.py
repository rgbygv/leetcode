# Created by Jones at 2023/11/05 12:12
# leetgo: dev
# https://leetcode.cn/problems/find-the-winner-of-an-array-game/

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
    def getWinner(self, arr: List[int], k: int) -> int:
        n = len(arr)

        if k >= n - 1:
            return max(arr)

        pre = arr[0]
        cnt = 0
        for i in range(1, n):
            x = arr[i]
            if x > pre:
                pre = x
                cnt = 1
            else:
                cnt += 1
            if cnt >= k:
                return pre

        return pre


# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().getWinner(arr, k)

    print("\noutput:", serialize(ans))
