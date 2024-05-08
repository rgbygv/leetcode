# Created by Jones at 2024/05/08 13:45
# leetgo: 1.4.6
# https://leetcode.cn/problems/watering-plants/

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
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        res = 0
        rest = capacity
        for i, x in enumerate(plants):
            res += 1  # step to i position
            if rest < x:
                res += i + i
                rest = capacity
            rest -= x
        return res


# @lc code=end

if __name__ == "__main__":
    plants: List[int] = deserialize("List[int]", read_line())
    capacity: int = deserialize("int", read_line())
    ans = Solution().wateringPlants(plants, capacity)
    print("\noutput:", serialize(ans, "integer"))
