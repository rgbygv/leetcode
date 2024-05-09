# Created by Jones at 2024/05/09 15:39
# leetgo: 1.4.6
# https://leetcode.cn/problems/sell-diminishing-valued-colored-balls/

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
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        """
        - `1 <= inventory.length <= 10⁵`
        - `1 <= inventory[i] <= 10⁹`
        - `1 <= orders <= min(sum(inventory[i]), 10⁹)`
        """
        mod = 10**9 + 7
        inventory.sort(reverse=True)
        inventory.append(0)

        def calc(x, y):
            """sum(range(x+1,y+1))"""
            x += 1
            return (x + y) * (y - x + 1) // 2 % mod

        res = 0
        for i, (x, y) in enumerate(pairwise(inventory), 1):
            if (tmp := i * (x - y)) > orders:
                # find i * (x-key) >= orders
                # key <= x - orders // i
                key = x - orders // i
                while i * (x - key) < orders:
                    key -= 1
                res += i * calc(key, x) % mod
                res += (orders - i * (x - key)) * (key + 1)
                res %= mod
                break
            else:
                orders -= tmp
                res += i * calc(y, x) % mod
                res %= mod
        return res % mod


# @lc code=end

if __name__ == "__main__":
    inventory: List[int] = deserialize("List[int]", read_line())
    orders: int = deserialize("int", read_line())
    ans = Solution().maxProfit(inventory, orders)
    print("\noutput:", serialize(ans, "integer"))
