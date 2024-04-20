# Created by Jones at 2024/04/20 20:31
# leetgo: 1.4.5
# https://leetcode.cn/problems/minimum-total-distance-traveled/

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
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        # we should split m robot to as most n factory

        # now we hace n place to set robot
        q = [pos for pos, cnt in factory for _ in range(cnt)]
        m, n = len(robot), len(q)

        @cache
        def dfs(i: int, j: int):
            """
            we should use q[..=j] to set robot[..=i]
            """
            if i == m:
                return 0

            if j == n or n - j < m - i:
                return inf

            # don't place robot[i] in factory[j]
            op1 = dfs(i, j + 1)
            # set robot[i] in factory[j]
            op2 = abs(robot[i] - q[j]) + dfs(i + 1, j + 1)
            return min(op1, op2)

        res = dfs(0, 0)
        dfs.cache_clear()
        return res


# @lc code=end

if __name__ == "__main__":
    robot: List[int] = deserialize("List[int]", read_line())
    factory: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().minimumTotalDistance(robot, factory)
    print("\noutput:", serialize(ans, "long"))
