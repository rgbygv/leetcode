# Created by Jones at 2024/05/22 10:13
# leetgo: 1.4.7
# https://leetcode.cn/problems/find-players-with-zero-or-one-losses/

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
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        deg = Counter()
        for x, y in matches:
            deg[x] += 0
            deg[y] += 1
        res = [[] for _ in range(2)]

        for k, d in deg.items():
            if d == 0:
                res[0].append(k)
            elif d == 1:
                res[1].append(k)
        for v in res:
            v.sort()
        return res


# @lc code=end

if __name__ == "__main__":
    matches: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().findWinners(matches)
    print("\noutput:", serialize(ans, "integer[][]"))
