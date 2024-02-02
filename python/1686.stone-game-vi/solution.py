# Created by Jones at 2024/02/02 12:57
# leetgo: 1.4.1
# https://leetcode.cn/problems/stone-game-vi/

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
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        q = []
        for x, y in zip(aliceValues, bobValues):
            # q.append((max(abs(x), abs(y)), x, y))
            item = (x + y, x, y)
            q.append(item)
        q.sort(reverse=True)

        res = 0
        for i, (_, x, y) in enumerate(q):
            if i & 1 == 0:
                res += x
            else:
                res -= y

        if res > 0:
            return 1
        elif res == 0:
            return 0
        else:
            return -1


# @lc code=end

if __name__ == "__main__":
    aliceValues: List[int] = deserialize("List[int]", read_line())
    bobValues: List[int] = deserialize("List[int]", read_line())
    ans = Solution().stoneGameVI(aliceValues, bobValues)
    print("\noutput:", serialize(ans, "integer"))
