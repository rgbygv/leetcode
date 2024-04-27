# Created by Jones at 2024/04/27 22:19
# leetgo: 1.4.5
# https://leetcode.cn/problems/find-the-shortest-superstring/

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
from pprint import pprint
from string import ascii_lowercase
from typing import List, Optional

# @lc code=begin


class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        n = len(words)

        def handle(last: str, word: str):
            """last is the s[-20:], since len(word) < 20"""
            m = len(word)
            n = len(last)
            for i in range(min(m, n), -1, -1):
                if last[n - i :] == word[:i]:
                    d = m - i
                    last += word[i:]
                    break
            # print(last, d)
            return last, d

        st = []

        @cache
        def dfs(mask: int, last: str):
            if mask == 0:
                return 0
            res = inf
            for i in range(n):
                if mask >> i & 1:
                    _last, d = handle(last, words[i])
                    cur = d + dfs(mask ^ (1 << i), _last)
                    if cur < res:
                        res = cur

            return res

        min_length = dfs((1 << n) - 1, "")
        print(min_length)

        return ""


# @lc code=end

if __name__ == "__main__":
    words: List[str] = deserialize("List[str]", read_line())
    ans = Solution().shortestSuperstring(words)
    print("\noutput:", serialize(ans, "string"))
