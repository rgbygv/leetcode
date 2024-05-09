# Created by Jones at 2024/05/09 14:45
# leetgo: 1.4.6
# https://leetcode.cn/problems/watering-plants-ii/

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
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        n = len(plants)
        l, r = 0, n - 1
        res = 0
        A, B = capacityA, capacityB
        while l <= r:
            if l == r:
                if max(A, B) < plants[l]:
                    res += 1
                break
            if A < plants[l]:
                res += 1
                A = capacityA
            A -= plants[l]
            l += 1

            if B < plants[r]:
                res += 1
                B = capacityB
            B -= plants[r]
            r -= 1
        return res


# @lc code=end

if __name__ == "__main__":
    plants: List[int] = deserialize("List[int]", read_line())
    capacityA: int = deserialize("int", read_line())
    capacityB: int = deserialize("int", read_line())
    ans = Solution().minimumRefill(plants, capacityA, capacityB)
    print("\noutput:", serialize(ans, "integer"))
