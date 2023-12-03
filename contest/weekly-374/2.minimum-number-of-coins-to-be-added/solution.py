# Created by Jones at 2023/12/03 10:30
# leetgo: dev
# https://leetcode.cn/problems/minimum-number-of-coins-to-be-added/
# https://leetcode.cn/contest/weekly-contest-374/problems/minimum-number-of-coins-to-be-added/

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
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        coins.sort()
        res = 0
        # 1-4 16

        """
        4 16

        """
        pre = 0
        for x in coins:
            while pre + 1 < x:
                res += 1
                pre = pre * 2 + 1
                if pre >= target:
                    return res
            pre += x
            if pre >= target:
                return res
        while pre + 1 <= target:
            res += 1
            pre = pre * 2 + 1
            if pre >= target:
                return res


# @lc code=end

if __name__ == "__main__":
    coins: List[int] = deserialize("List[int]", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().minimumAddedCoins(coins, target)

    print("\noutput:", serialize(ans))
