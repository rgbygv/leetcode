# Created by Jones at 2024/06/12 13:22
# leetgo: 1.4.7
# https://leetcode.cn/problems/account-balance-after-rounded-purchase/

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
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        res = 100 - purchaseAmount

        rest = res % 10
        if rest % 10 == 5:
            return res - 5
        if rest % 10 == 0:
            return res
        if rest > 5:
            return res - rest + 10
        return res - rest

        return res - res % 10


# @lc code=end

if __name__ == "__main__":
    purchaseAmount: int = deserialize("int", read_line())
    ans = Solution().accountBalanceAfterPurchase(purchaseAmount)
    print("\noutput:", serialize(ans, "integer"))
