# Created by Jones at 2024/05/05 20:55
# leetgo: 1.4.6
# https://leetcode.cn/problems/minimum-length-of-anagram-concatenation/
# https://leetcode.cn/contest/weekly-contest-396/problems/minimum-length-of-anagram-concatenation/

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
    def minAnagramLength(self, s: str) -> int:
        cnt = Counter(s)
        m = len(s)
        if min(cnt.values()) == 1:
            return m
        # if s is formed by t, t's size is n
        # 0..n n..2n  ..m

        # mn = min(cnt.values())

        for size in range(1, m + 1):
            ok = m % size == 0
            if ok:
                t = sorted(s[:size])
                if all(sorted(s[i : i + size]) == t for i in range(size, m, size)):
                    return size
        return m


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().minAnagramLength(s)
    print("\noutput:", serialize(ans, "integer"))
