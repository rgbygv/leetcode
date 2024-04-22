# Created by Jones at 2024/04/22 13:47
# leetgo: 1.4.5
# https://leetcode.com/problems/open-the-lock/

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
from pprint import pprint
from string import ascii_lowercase
from typing import List, Optional

# @lc code=begin


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # - `1 <= deadends.length <= 500`
        # - `deadends[i].length == 4`
        # - `target.length == 4`
        # - target **will not be** in the list `deadends`.
        # - `target` and `deadends[i]` consist of digits only.
        start = "0" * 4
        if target == start:
            return 0
        ban = set(deadends)
        if start in ban:
            return -1

        """
        minimum use bfs
        """

        q = deque()
        q.append("0" * 4)
        t = 0
        while q:
            t += 1  # we have checked 0, so at least we need change once
            n = len(q)
            for _ in range(n):
                start = list(map(int, q.popleft()))
                for i in range(4):
                    for x in (-1, 1):
                        c = start.copy()
                        c[i] = (c[i] + x) % 10  # 9 -> 0
                        end = "".join(map(str, c))
                        if end == target:
                            return t
                        if end not in ban:
                            ban.add(end)
                            q.append(end)
        return -1


# @lc code=end

if __name__ == "__main__":
    deadends: List[str] = deserialize("List[str]", read_line())
    target: str = deserialize("str", read_line())
    ans = Solution().openLock(deadends, target)
    print("\noutput:", serialize(ans, "integer"))
