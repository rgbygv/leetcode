# Created by Jones at 2024/04/25 14:04
# leetgo: 1.4.5
# https://leetcode.cn/problems/total-distance-traveled/

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
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        res = 0
        while mainTank >= 5:
            a, b = divmod(mainTank, 5)
            res += a * 5
            mainTank = b + min(additionalTank, a)
            additionalTank = max(0, additionalTank - a)

        return (mainTank + res) * 10


# @lc code=end

if __name__ == "__main__":
    mainTank: int = deserialize("int", read_line())
    additionalTank: int = deserialize("int", read_line())
    ans = Solution().distanceTraveled(mainTank, additionalTank)
    print("\noutput:", serialize(ans, "integer"))
