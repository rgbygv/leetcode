# Created by Jones at 2024/06/02 12:14
# leetgo: 1.4.7
# https://leetcode.cn/problems/distribute-candies/

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
    def distributeCandies(self, candyType: List[int]) -> int:
        return min(len(set(candyType)), len(candyType) // 2)


# @lc code=end

if __name__ == "__main__":
    candyType: List[int] = deserialize("List[int]", read_line())
    ans = Solution().distributeCandies(candyType)
    print("\noutput:", serialize(ans, "integer"))
