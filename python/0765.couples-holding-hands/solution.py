# Created by Jones at 2023/11/11 19:31
# leetgo: dev
# https://leetcode.cn/problems/couples-holding-hands/

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
    def minSwapsCouples(self, row: List[int]) -> int:
        mp = {v: i for i, v in enumerate(row)}
        res = 0
        for i in range(0, len(row), 2):
            j = mp[row[i] ^ 1]
            if j != i + 1:
                mp[row[i + 1]] = j
                row[j] = row[i + 1]
                res += 1
        return res


# @lc code=end

if __name__ == "__main__":
    row: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minSwapsCouples(row)

    print("\noutput:", serialize(ans))
