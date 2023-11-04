# Created by Jones at 2023/11/03 20:25
# leetgo: dev
# https://leetcode.cn/problems/build-an-array-with-stack-operations/

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
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        i = 1
        for x in target:
            while i != x:
                res.append("Push")
                res.append("Pop")
                i += 1
            res.append("Push")
            i += 1
        return res


# @lc code=end

if __name__ == "__main__":
    target: List[int] = deserialize("List[int]", read_line())
    n: int = deserialize("int", read_line())
    ans = Solution().buildArray(target, n)

    print("\noutput:", serialize(ans))
