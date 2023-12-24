# Created by Jones at 2023/12/24 22:16
# leetgo: dev
# https://leetcode.cn/problems/maximum-square-area-by-removing-fences-from-a-field/
# https://leetcode.cn/contest/weekly-contest-377/problems/maximum-square-area-by-removing-fences-from-a-field/

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
    def maximizeSquareArea(self, m: int, n: int, H: List[int], V: List[int]) -> int:
        H = [1] + H + [m]
        V = [1] + V + [n]

        def f(h):
            seen = set()
            for x in h:
                for y in h:
                    seen.add(abs(x - y))
            return seen

        s1 = f(H)
        s2 = f(V)

        x = max(s1 & s2, default=0)
        if x == 0:
            return -1
        return x * x % (10 ** 9 + 7)


# @lc code=end

if __name__ == "__main__":
    m: int = deserialize("int", read_line())
    n: int = deserialize("int", read_line())
    hFences: List[int] = deserialize("List[int]", read_line())
    vFences: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maximizeSquareArea(m, n, hFences, vFences)

    print("\noutput:", serialize(ans))
