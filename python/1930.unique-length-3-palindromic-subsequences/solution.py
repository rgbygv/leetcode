# Created by Jones at 2023/11/14 20:20
# leetgo: dev
# https://leetcode.cn/problems/unique-length-3-palindromic-subsequences/

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
    def countPalindromicSubsequence(self, s: str) -> int:
        mp = defaultdict(list)
        for i, ch in enumerate(s):
            mp[ch].append(i)

        res = 0
        for mid in mp:
            v = mp[mid]
            for left in mp:
                cur = mp[left]
                if len(cur) < 2:
                    continue
                if any(cur[0] < i < cur[-1] for i in v):
                    res += 1
        return res


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().countPalindromicSubsequence(s)

    print("\noutput:", serialize(ans))
