# Created by Jones at 2024/05/07 13:45
# leetgo: 1.4.6
# https://leetcode.cn/problems/find-the-longest-substring-containing-vowels-in-even-counts/

from typing import *
from leetgo_py import *

from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from functools import cache, cmp_to_key, lru_cache, reduce
from heapq import heapify, heappop, heappush, heappushpop, heapreplace
from icecream import ic
from itertools import accumulate, chain, count, pairwise, zip_longest
from math import ceil, comb, floor, gcd, inf, isqrt, lcm, log2, perm, sqrt
from operator import xor
from pprint import pprint
from string import ascii_lowercase
from typing import List, Optional

# @lc code=begin


class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        mask = 0
        idx = {v: i for i, v in enumerate("aeiou")}
        res = 0
        mp = {0: 0}

        for i, ch in enumerate(s, 1):
            if ch in idx:
                mask ^= 1 << idx[ch]
            if mask in mp:
                res = max(res, i - mp[mask])
            else:
                mp[mask] = i
        return res


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().findTheLongestSubstring(s)
    print("\noutput:", serialize(ans, "integer"))
