# Created by Jones at 2023/12/10 16:15
# leetgo: dev
# https://leetcode.cn/problems/count-tested-devices-after-test-operations/
# https://leetcode.cn/contest/weekly-contest-375/problems/count-tested-devices-after-test-operations/

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
from string import ascii_lowercase
from typing import List, Optional

# @lc code=begin
# from sortedcontainers import SortedList


class Solution:
    def countTestedDevices(self, a: List[int]) -> int:
        n = len(a)
        res = 0
        for i in range(n):
            if a[i] > 0:
                res += 1
                for j in range(i + 1, n):
                    a[j] -= 1
        return res


# @lc code=end

if __name__ == "__main__":
    batteryPercentages: List[int] = deserialize("List[int]", read_line())
    ans = Solution().countTestedDevices(batteryPercentages)

    print("\noutput:", serialize(ans))
