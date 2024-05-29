# Created by Jones at 2024/05/29 12:50
# leetgo: 1.4.7
# https://leetcode.cn/problems/find-longest-special-substring-that-occurs-thrice-i/

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
    def maximumLength(self, s: str) -> int:
        """
        - `3 <= s.length <= 50`
        - `s` consists of only lowercase English letters.
        """

        n = len(s)
        cnt = Counter()
        for l in range(n):
            cur = s[l]
            cnt[cur] += 1
            r = l + 1
            while r < n and s[r] == s[l]:
                cur += s[r]
                cnt[cur] += 1
                r += 1
            l = r

        res = -1
        for sub, c in cnt.items():
            if c >= 3:
                res = max(res, len(sub))
        return res

        # wrong
        max_size = n - 2

        for size in range(max_size, 0, -1):
            for i in range(n - size + 1):
                sub = s[i : i + size]
                for j in range(i + 1, n - size + 1):
                    if s[j : j + size] == sub and sub in s[j + 1 :]:
                        return size

        return -1


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().maximumLength(s)
    print("\noutput:", serialize(ans, "integer"))
