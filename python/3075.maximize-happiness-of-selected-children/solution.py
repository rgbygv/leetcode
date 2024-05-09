# Created by Jones at 2024/05/09 14:54
# leetgo: 1.4.6
# https://leetcode.com/problems/maximize-happiness-of-selected-children/

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
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()
        d = 0
        res = 0
        n = len(happiness)
        for i in reversed(range(n - k, n)):
            res += max(0, happiness[i] - d)
            d += 1
        return res


# @lc code=end

if __name__ == "__main__":
    happiness: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().maximumHappinessSum(happiness, k)
    print("\noutput:", serialize(ans, "long"))
