# Created by Jones at 2024/05/14 16:31
# leetgo: 1.4.7
# https://leetcode.cn/problems/minimum-rounds-to-complete-all-tasks/

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
    def minimumRounds(self, tasks: List[int]) -> int:
        res = 0
        for v in Counter(tasks).values():
            if v == 1:
                return -1
            res += (v + 2) // 3
        return res


# @lc code=end

if __name__ == "__main__":
    tasks: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minimumRounds(tasks)
    print("\noutput:", serialize(ans, "integer"))
