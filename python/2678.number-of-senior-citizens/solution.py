# Created by Jones at 2023/10/23 12:29
# leetgo: dev
# https://leetcode.cn/problems/number-of-senior-citizens/

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
    def countSeniors(self, details: List[str]) -> int:
        return sum(int(d[11:13]) > 60 for d in details)


# @lc code=end

if __name__ == "__main__":
    details: List[str] = deserialize("List[str]", read_line())
    ans = Solution().countSeniors(details)

    print("\noutput:", serialize(ans))
