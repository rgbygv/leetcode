# Created by Jones at 2023/12/10 16:15
# leetgo: dev
# https://leetcode.cn/problems/double-modular-exponentiation/
# https://leetcode.cn/contest/weekly-contest-375/problems/double-modular-exponentiation/

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
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        return [
            i
            for i, (a, b, c, m) in enumerate(variables)
            if pow(pow(a, b, 10), c, m) == target
        ]


# @lc code=end

if __name__ == "__main__":
    variables: List[List[int]] = deserialize("List[List[int]]", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().getGoodIndices(variables, target)

    print("\noutput:", serialize(ans))
