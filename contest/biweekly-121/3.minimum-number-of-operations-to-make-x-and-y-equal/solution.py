# Created by Jones at 2024/01/06 22:30
# leetgo: dev
# https://leetcode.cn/problems/minimum-number-of-operations-to-make-x-and-y-equal/
# https://leetcode.cn/contest/biweekly-contest-121/problems/minimum-number-of-operations-to-make-x-and-y-equal/

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
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        if x == y:
            return 0
        N = 11 * 10**4 + 1
        seen = set()
        q = [x]
        for cnt in count(0):
            nxt = []
            for x in q:
                if x == y:
                    return cnt
                if x in seen:
                    continue
                seen.add(x)
                if x % 11 == 0 and (x // 11) not in seen:
                    nxt.append(x // 11)
                if x % 5 == 0 and (x // 5) not in seen:
                    nxt.append(x // 5)
                if (x - 1) not in seen:
                    nxt.append(x - 1)
                if (x + 1) not in seen and x + 1 < N:
                    nxt.append(x + 1)
            q = nxt


# @lc code=end

if __name__ == "__main__":
    x: int = deserialize("int", read_line())
    y: int = deserialize("int", read_line())
    ans = Solution().minimumOperationsToMakeEqual(x, y)

    print("\noutput:", serialize(ans))
