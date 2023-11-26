# Created by Jones at 2023/11/26 15:21
# leetgo: dev
# https://leetcode.cn/problems/count-unique-characters-of-all-substrings-of-a-given-string/

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
    def uniqueLetterString(self, s: str) -> int:
        res = 0
        mp = defaultdict(lambda: [-1])

        for i, ch in enumerate(s):
            mp[ch].append(i)

        n = len(s)
        for ch in mp:
            mp[ch].append(n)

        for v in mp.values():
            pre = 0
            for x, y in pairwise(v):
                res += pre * (y - x)
                pre = y - x
        return res


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().uniqueLetterString(s)

    print("\noutput:", serialize(ans))
