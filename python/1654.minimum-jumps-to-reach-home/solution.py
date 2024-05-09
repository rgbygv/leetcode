# Created by Jones at 2024/05/09 18:29
# leetgo: 1.4.6
# https://leetcode.cn/problems/minimum-jumps-to-reach-home/

from typing import *
from leetgo_py import *

from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from functools import cache, cmp_to_key, lru_cache, reduce
from heapq import heapify, heappop, heappush, heappushpop, heapreplace
from icecream import ic
from itertools import accumulate, chain, count, pairwise, zip_longest
from math import ceil, comb, floor, gcd, inf, isqrt, lcm, log2, perm, sqrt
from operator import xor
from pprint import pprint
from string import ascii_lowercase
from typing import List, Optional

# @lc code=begin


class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, target: int) -> int:
        """
        - `1 <= forbidden.length <= 1000`
        - `1 <= a, b, forbidden[i] <= 2000`
        - `0 <= x <= 2000`
        - All the elements in `forbidden` are distinct.
        - Position `x` is not forbidden.
        """
        if target == 0:
            return 0
        ban = set(forbidden)
        N = 2000 * 3 + 1
        q = [(0, 0)]
        vis = set()
        vis.add(q[0])
        t = 0
        while q:
            t += 1
            nxt = []
            for x, cnt in q:
                y = x + a
                if 0 <= y < N and y not in ban and (y, 0) not in vis:
                    if y == target:
                        return t
                    vis.add((y, 0))
                    nxt.append((y, 0))
                if cnt == 0:
                    y = x - b
                    if 0 <= y < N and y not in ban and (y, 1) not in vis:
                        if y == target:
                            return t
                        vis.add((y, 1))
                        nxt.append((y, 1))
            q = nxt
        return -1


# @lc code=end

if __name__ == "__main__":
    forbidden: List[int] = deserialize("List[int]", read_line())
    a: int = deserialize("int", read_line())
    b: int = deserialize("int", read_line())
    x: int = deserialize("int", read_line())
    ans = Solution().minimumJumps(forbidden, a, b, x)
    print("\noutput:", serialize(ans, "integer"))
