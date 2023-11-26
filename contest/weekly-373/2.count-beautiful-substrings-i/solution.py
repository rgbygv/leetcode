# Created by Jones at 2023/11/26 10:30
# leetgo: dev
# https://leetcode.cn/problems/count-beautiful-substrings-i/
# https://leetcode.cn/contest/weekly-contest-373/problems/count-beautiful-substrings-i/

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
    def beautifulSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        res = 0
        s = [ch in "aeiou" for ch in s]
        # print(s)

        for i in range(n):
            c1 = c2 = 0
            for j in range(i, -1, -1):
                if s[j]:
                    c1 += 1
                else:
                    c2 += 1
                if c1 == 0 or c2 == 0:
                    continue
                elif c1 == c2 and c2 * c2 % k == 0:
                    res += 1
        return res


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().beautifulSubstrings(s, k)

    print("\noutput:", serialize(ans))
