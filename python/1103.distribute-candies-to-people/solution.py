# Created by Jones at 2024/06/03 10:17
# leetgo: 1.4.7
# https://leetcode.cn/problems/distribute-candies-to-people/

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
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        q = [0] * num_people
        i = 0
        while candies > 0:
            q[i % num_people] += min(candies, i + 1)
            i += 1
            candies -= i
        return q


# @lc code=end

if __name__ == "__main__":
    candies: int = deserialize("int", read_line())
    num_people: int = deserialize("int", read_line())
    ans = Solution().distributeCandies(candies, num_people)
    print("\noutput:", serialize(ans, "integer[]"))
