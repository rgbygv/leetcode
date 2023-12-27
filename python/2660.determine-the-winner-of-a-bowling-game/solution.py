# Created by Bob at 2023/12/27 14:57
# leetgo: dev
# https://leetcode.cn/problems/determine-the-winner-of-a-bowling-game/

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
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        def cal(scores: list[int]):
            res = 0
            for i, x in enumerate(scores):
                if i > 0 and scores[i - 1] == 10 or i > 1 and scores[i - 2] == 10:
                    res += 2 * x
                else:
                    res += x
            return res

        s1 = cal(player1)
        s2 = cal(player2)

        match s1 - s2:
            case 0:
                return 0
            case x if x > 0:
                return 1
            case _:
                return 2


# @lc code=end

if __name__ == "__main__":
    player1: List[int] = deserialize("List[int]", read_line())
    player2: List[int] = deserialize("List[int]", read_line())
    ans = Solution().isWinner(player1, player2)

    print("\noutput:", serialize(ans))
