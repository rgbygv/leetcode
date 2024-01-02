# Created by Bob at 2024/01/02 13:32
# leetgo: dev
# https://leetcode.cn/problems/count-the-repetitions/

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


class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        set1 = set(s1)
        set2 = set(s2)

        if set1 & set2 != set2:
            return 0

        s1 = "".join(ch for ch in s1 if ch in set2)

        m, n = len(s1), len(s2)

        # 1 s2 -> cnt1, i1
        # 2 s2 -> cnt2, i2
        # ...
        # j s2 -> cntj, 0

        mp = {}

        cnt1 = cnt2 = i = 0
        while True:
            cnt1 += 1
            for ch in s1:
                if ch == s2[i]:
                    i += 1
                    if i == n:
                        cnt2 += 1
                        i = 0
            if cnt1 == n1:
                return cnt2 // n2
            # must exist
            if i in mp:
                p1, p2 = mp[i]
                loop = (cnt1 - p1, cnt2 - p2)
                break
            mp[i] = (cnt1, cnt2)

        pre = p2  # before loop
        in_loop = (n1 - p1) // (loop[0]) * loop[1]

        res = pre + in_loop

        for _ in range((n1 - p1) % loop[0]):
            for ch in s1:
                if ch == s2[i]:
                    i += 1
                    if i == n:
                        res += 1
                        i = 0
        return res // n2


# @lc code=end

if __name__ == "__main__":
    s1: str = deserialize("str", read_line())
    n1: int = deserialize("int", read_line())
    s2: str = deserialize("str", read_line())
    n2: int = deserialize("int", read_line())
    ans = Solution().getMaxRepetitions(s1, n1, s2, n2)

    print("\noutput:", serialize(ans))
