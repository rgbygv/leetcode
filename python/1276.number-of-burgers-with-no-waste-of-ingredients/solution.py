# Created by Jones at 2023/12/25 20:39
# leetgo: dev
# https://leetcode.cn/problems/number-of-burgers-with-no-waste-of-ingredients/

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
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        if tomatoSlices < cheeseSlices * 2:
            return []

        if tomatoSlices & 1:
            return []

        a = (tomatoSlices - 2 * cheeseSlices) // 2

        # a * 4 + (cheeseSlices- a) * 2 == tomatoSlices

        if 0 <= a <= cheeseSlices:
            return [a, cheeseSlices - a]
        return []

        # a use 2 tomato more then che


# @lc code=end

if __name__ == "__main__":
    tomatoSlices: int = deserialize("int", read_line())
    cheeseSlices: int = deserialize("int", read_line())
    ans = Solution().numOfBurgers(tomatoSlices, cheeseSlices)

    print("\noutput:", serialize(ans))
