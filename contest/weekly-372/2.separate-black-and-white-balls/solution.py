# Created by Jones at 2023/11/19 10:30
# leetgo: dev
# https://leetcode.cn/problems/separate-black-and-white-balls/
# https://leetcode.cn/contest/weekly-contest-372/problems/separate-black-and-white-balls/

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
    def minimumSteps(self, s: str) -> int:
        i = 0
        res = 0
        for j, ch in enumerate(s):
            if ch == "0":
                res += j - i
                i += 1
        return res


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().minimumSteps(s)

    print("\noutput:", serialize(ans))
