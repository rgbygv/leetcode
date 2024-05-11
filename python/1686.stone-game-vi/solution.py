# Created by Jones at 2024/05/11 14:29
# leetgo: 1.4.7
# https://leetcode.cn/problems/stone-game-vi/

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
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        q = sorted(
            ((x + y, x, y) for x, y in zip(aliceValues, bobValues)), reverse=True
        )
        res = 0
        for i, (_, x, y) in enumerate(q):
            res += x if i & 1 == 0 else -y

        # wrong
        # @cache
        # def dfs(i: int, turn: bool):
        #     if i == n:
        #         return 0
        #     if turn:
        #         return max(
        #             aliceValues[i] - dfs(i + 1, not turn),
        #             -bobValues[i] + dfs(i + 1, turn),
        #         )
        #     else:
        #         return min(
        #             bobValues[i] - dfs(i + 1, not turn),
        #             -aliceValues[i] + dfs(i + 1, turn),
        #         )

        # res = dfs(0, True)

        if res > 0:
            return 1
        return -1 if res < 0 else 0


# @lc code=end

if __name__ == "__main__":
    aliceValues: List[int] = deserialize("List[int]", read_line())
    bobValues: List[int] = deserialize("List[int]", read_line())
    ans = Solution().stoneGameVI(aliceValues, bobValues)
    print("\noutput:", serialize(ans, "integer"))
