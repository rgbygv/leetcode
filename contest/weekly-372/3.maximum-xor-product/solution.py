# Created by Jones at 2023/11/19 10:30
# leetgo: dev
# https://leetcode.cn/problems/maximum-xor-product/
# https://leetcode.cn/contest/weekly-contest-372/problems/maximum-xor-product/

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
    def maximumXorProduct(self, a: int, b: int, n: int) -> int:
        if a > b:
            a, b = b, a
        for i in range(n - 1, -1, -1):
            if a >> i & 1 == 0:
                a ^= 1 << i
                b ^= 1 << i
            if a > b:
                a, b = b, a
        return a * b % (10**9 + 7)


# @lc code=end

if __name__ == "__main__":
    a: int = deserialize("int", read_line())
    b: int = deserialize("int", read_line())
    n: int = deserialize("int", read_line())
    ans = Solution().maximumXorProduct(a, b, n)

    print("\noutput:", serialize(ans))
