# Created by Jones at 2024/05/20 13:44
# leetgo: 1.4.7
# https://leetcode.cn/problems/find-longest-awesome-substring/

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
    def longestAwesome(self, s: str) -> int:
        mp = {0: 0}
        mask = 0
        res = 0
        for i, ch in enumerate(s, 1):
            mask ^= 1 << int(ch)
            if mask.bit_count() <= 1:
                res = max(res, i)
            for v in range(10):
                valid = 1 << v
                if (pre := mask ^ valid) in mp:
                    res = max(res, i - mp[pre])
            if mask not in mp:
                mp[mask] = i
        return res


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().longestAwesome(s)
    print("\noutput:", serialize(ans, "integer"))
