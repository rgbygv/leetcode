# Created by Jones at 2024/05/15 19:39
# leetgo: 1.4.7
# https://leetcode.cn/problems/minimum-time-to-complete-all-tasks/

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
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        """
        - `1 <= tasks.length <= 2000`
        - `tasks[i].length == 3`
        - `1 <= startᵢ, endᵢ <= 2000`
        - `1 <= durationᵢ <= endᵢ - startᵢ + 1 `
        """
        tasks.sort()
        n = len(tasks)
        N = max(y for _, y, _ in tasks)
        diff = [0] * (N + 2)
        for x, y, _ in tasks:
            diff[x] += 1
            diff[y + 1] -= 1
        ic(list(accumulate(diff)))


# @lc code=end

if __name__ == "__main__":
    tasks: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().findMinimumTime(tasks)
    print("\noutput:", serialize(ans, "integer"))
