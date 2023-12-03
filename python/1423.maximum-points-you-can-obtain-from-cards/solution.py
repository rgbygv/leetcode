# Created by Jones at 2023/12/03 14:26
# leetgo: dev
# https://leetcode.cn/problems/maximum-points-you-can-obtain-from-cards/

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
    def maxScore(self, a: List[int], k: int) -> int:
        if k == len(a):
            return sum(a)

        k = len(a) - k
        # find minimal a[i:i+n-k]
        s = sum(a[: k - 1])
        mn = inf
        for i in range(k - 1, len(a)):
            s += a[i]
            mn = min(s, mn)
            s -= a[i - (k - 1)]
        return sum(a) - mn


# @lc code=end

if __name__ == "__main__":
    cardPoints: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().maxScore(cardPoints, k)

    print("\noutput:", serialize(ans))
