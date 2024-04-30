# Created by Jones at 2024/04/30 12:42
# leetgo: 1.4.5
# https://leetcode.cn/problems/number-of-employees-who-met-the-target/

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
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        return sum(x >= target for x in hours)


# @lc code=end

if __name__ == "__main__":
    hours: List[int] = deserialize("List[int]", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().numberOfEmployeesWhoMetTarget(hours, target)
    print("\noutput:", serialize(ans, "integer"))
