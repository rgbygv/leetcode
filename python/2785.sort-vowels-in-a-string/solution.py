# Created by Jones at 2023/11/13 19:36
# leetgo: dev
# https://leetcode.cn/problems/sort-vowels-in-a-string/

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
    def sortVowels(self, s: str) -> str:
        vow = "aeiou"
        val = sorted((ch for ch in s if ch.lower() in vow), reverse=True)

        res = []
        for ch in s:
            if ch.lower() in vow:
                res.append(val.pop())
            else:
                res.append(ch)
        return "".join(res)


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().sortVowels(s)

    print("\noutput:", serialize(ans))
