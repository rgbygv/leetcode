# Created by Jones at 2024/05/29 14:05
# leetgo: 1.4.7
# https://leetcode.cn/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/

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
    def minFlips(self, s: str) -> int:
        # how to use op1 to decrease answer
        # just brute force do op1 for all s[i]
        # we need a sliding window to change useless compute
        # we let s be 010101
        n = len(s)
        cnt = 0
        for i, ch in enumerate(s):
            cnt += (int(ch) & 1) != (i & 1)
        res = min(cnt, n - cnt)
        # sliding window, del front then add it to end
        for i, ch in enumerate(s):
            ch = int(ch)
            cnt -= ch != (i & 1)
            cnt += ch != ((i + n) & 1)
            res = min(res, cnt, n - cnt)
        return res

        # below situation is hard to understand
        s += s
        n = len(s)

        f = [0] * n  # keep s[i] = 1 and s is special
        g = [0] * n  # keep s[i] = 0 and ..

        # and f[i] = n - g[i]

        f[0] = int(s[0] == "0")
        g[0] = int(s[0] == "1")

        for i in range(1, n):
            if s[i] == "1":
                f[i] = g[i - 1]
                g[i] = 1 + f[i - 1]
            else:
                g[i] = f[i - 1]
                f[i] = 1 + g[i - 1]
        # ic(f, g)
        m = n // 2
        res = min(f[m - 1], g[m - 1])
        for i in range(m):
            # ic(res, f[i + m] - g[i], g[i + m] - f[i])
            if m & 1:
                res = min(res, f[i + m] - g[i], g[i + m] - f[i])
            else:
                res = min(res, m - (f[i + m] - f[i]), m - (g[i + m] - g[i]))
        return res


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().minFlips(s)
    print("\noutput:", serialize(ans, "integer"))
