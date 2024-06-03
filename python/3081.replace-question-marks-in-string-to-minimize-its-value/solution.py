# Created by Jones at 2024/06/03 15:43
# leetgo: 1.4.7
# https://leetcode.cn/problems/replace-question-marks-in-string-to-minimize-its-value/

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
    def minimizeStringValue(self, s: str) -> str:
        t = []
        q = []
        cnt = Counter(ch for ch in s if ch != "?")
        for ch in ascii_lowercase:
            heappush(q, (cnt[ch], ch))
        for ch in s:
            if ch == "?":
                _, ch = heappop(q)
                t.append(ch)
                cnt[ch] += 1
                heappush(q, (cnt[ch], ch))
        t.sort(reverse=True)
        res = list(s)
        for i, ch in enumerate(res):
            if ch == "?":
                res[i] = t.pop()
        return "".join(res)


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().minimizeStringValue(s)
    print("\noutput:", serialize(ans, "string"))
