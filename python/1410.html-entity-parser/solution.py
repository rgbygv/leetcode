# Created by Jones at 2023/11/23 14:36
# leetgo: dev
# https://leetcode.cn/problems/html-entity-parser/

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
    def entityParser(self, text: str) -> str:
        mp = {
            "&quot;": '"',
            "&apos;": "'",
            "&gt;": ">",
            "&lt;": "<",
            "&frasl;": "/",
            "&amp;": "&",
        }
        n = len(text)
        i = 0
        res = []
        while i < n:
            ok = False
            if text[i] == "&":
                for j in range(4, 8):
                    cur = text[i : i + j]
                    if cur in mp:
                        res.append(mp[cur])
                        i += j
                        ok = True
                        break
            if not ok:
                res.append(text[i])
                i += 1
        return "".join(res)


# @lc code=end

if __name__ == "__main__":
    text: str = deserialize("str", read_line())
    ans = Solution().entityParser(text)

    print("\noutput:", serialize(ans))
