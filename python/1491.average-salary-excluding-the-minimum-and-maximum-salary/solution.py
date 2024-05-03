# Created by Jones at 2024/05/03 13:30
# leetgo: 1.4.5
# https://leetcode.cn/problems/average-salary-excluding-the-minimum-and-maximum-salary/

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
    def average(self, salary: List[int]) -> float:
        n = len(salary)
        return sum(sorted(salary)[1 : n - 1]) / (n - 2)


# @lc code=end

if __name__ == "__main__":
    salary: List[int] = deserialize("List[int]", read_line())
    ans = Solution().average(salary)
    print("\noutput:", serialize(ans, "double"))
