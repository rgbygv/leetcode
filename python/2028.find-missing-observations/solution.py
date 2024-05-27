# Created by Jones at 2024/05/27 08:14
# leetgo: 1.4.7
# https://leetcode.cn/problems/find-missing-observations/

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
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        s = sum(rolls)
        total = mean * (len(rolls) + n)
        if s + n * 6 < total:
            return []
        if s + n > total:
            return []
        target = total - s
        res = []
        for i in range(n):
            rest = n - i - 1
            for x in range(1, 7):
                if rest <= target - x <= rest * 6:
                    res.append(x)
                    target -= x
                    break
        return res


# @lc code=end

if __name__ == "__main__":
    rolls: List[int] = deserialize("List[int]", read_line())
    mean: int = deserialize("int", read_line())
    n: int = deserialize("int", read_line())
    ans = Solution().missingRolls(rolls, mean, n)
    print("\noutput:", serialize(ans, "integer[]"))
