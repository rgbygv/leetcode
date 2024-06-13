# Created by Jones at 2024/06/13 14:29
# leetgo: 1.4.7
# https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/

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
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        return sum(abs(x - y) for x, y in zip(sorted(seats), sorted(students)))


# @lc code=end

if __name__ == "__main__":
    seats: List[int] = deserialize("List[int]", read_line())
    students: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minMovesToSeat(seats, students)
    print("\noutput:", serialize(ans, "integer"))
