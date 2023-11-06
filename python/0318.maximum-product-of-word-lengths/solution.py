# Created by Jones at 2023/11/06 14:23
# leetgo: dev
# https://leetcode.cn/problems/maximum-product-of-word-lengths/

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
    def maxProduct(self, words: List[str]) -> int:
        words.sort(key=len, reverse=True)
        q = []
        for w in words:
            mask = 0
            for ch in w:
                mask |= 1 << (ord(ch) - ord("a"))
            q.append((len(w), mask))

        res = 0
        for i in range(len(words)):
            x_len, x = q[i]
            for j in range(i):
                y_len, y = q[j]
                if x_len * y_len <= res:
                    break
                if x & y == 0:
                    res = x_len * y_len
        return res
        # n = len(words)
        # ok = [[True] * n for _ in range(n)]

        # mp = defaultdict(list)
        # for i, w in enumerate(words):
        #     for ch in set(w):
        #         for j in mp[ch]:
        #             ok[j][i] = False
        #         mp[ch].append(i)

        # res = 0
        # for i in range(n):
        #     for j in range(i):
        #         if ok[j][i]:
        #             cur = len(words[i]) * len(words[j])
        #             if cur > res:
        #                 res = cur
        # return res

        # words.sort(key=len, reverse=True)

        # q = [(len(w), set(w)) for w in words]

        # res = 0
        # for i in range(len(words)):
        #     x_len, x = q[i]
        #     for j in range(i):
        #         y_len, y = q[j]
        #         if x_len * y_len <= res:
        #             break
        #         if not (x & y):
        #             res = x_len * y_len
        # return res


# @lc code=end

if __name__ == "__main__":
    words: List[str] = deserialize("List[str]", read_line())
    ans = Solution().maxProduct(words)

    print("\noutput:", serialize(ans))
