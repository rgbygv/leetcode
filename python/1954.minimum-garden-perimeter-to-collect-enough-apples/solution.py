# Created by Jones at 2023/12/24 20:58
# leetgo: dev
# https://leetcode.cn/problems/minimum-garden-perimeter-to-collect-enough-apples/

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
    def minimumPerimeter(self, neededApples: int) -> int:
        s = 0

        for a in count(1):
            s += 4 * (3 * a * a)
            if s >= neededApples:
                return a * 8

        return -1


# @lc code=end

if __name__ == "__main__":
    neededApples: int = deserialize("int", read_line())
    ans = Solution().minimumPerimeter(neededApples)

    print("\noutput:", serialize(ans))
