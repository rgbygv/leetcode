# Created by Bob at 2023/12/29 20:05
# leetgo: dev
# https://leetcode.cn/problems/buy-two-chocolates/

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
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()

        if (s := prices[0] + prices[1]) > money:
            return money
        return money - s


# @lc code=end

if __name__ == "__main__":
    prices: List[int] = deserialize("List[int]", read_line())
    money: int = deserialize("int", read_line())
    ans = Solution().buyChoco(prices, money)

    print("\noutput:", serialize(ans))
