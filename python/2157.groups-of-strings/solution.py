# Created by Jones at 2023/12/04 22:03
# leetgo: dev
# https://leetcode.cn/problems/groups-of-strings/

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


class UnionFind:
    def __init__(self, n) -> None:
        self.components = n
        self.fa = list(range(n))
        self.rank = [1] * n
        self.max_size = 1

    def find(self, x):
        if self.fa[x] != x:
            self.fa[x] = self.find(self.fa[x])
        return self.fa[x]

    def union(self, x, y):
        fx, fy = self.find(x), self.find(y)
        if fx == fy:
            return False
        if self.rank[fy] > self.rank[fx]:
            fx, fy = fy, fx
        self.fa[fy] = fx
        self.rank[fx] += self.rank[fy]
        self.max_size = max(self.max_size, self.rank[fx])
        self.components -= 1
        return True


class Solution:
    def groupStrings(self, words: List[str]) -> List[int]:
        n = len(words)
        uf = UnionFind(n)
        words.sort(key=len)

        def f(w) -> int:
            res = 0
            for ch in w:
                res |= 1 << (ord(ch) - ord("a"))
            return res

        words = [f(w) for w in words]

        mp = {}
        for i, x in enumerate(words):
            for d in range(26):
                if x >> d & 1 == 0:
                    continue
                y = x ^ (1 << d)
                # add
                if y in mp:
                    uf.union(i, mp[y])
                # replace
                for j in range(26):
                    tmp = y | (1 << j)
                    if tmp in mp:
                        uf.union(i, mp[tmp])
                        break
            mp[x] = i

        return [uf.components, uf.max_size]


# @lc code=end

if __name__ == "__main__":
    words: List[str] = deserialize("List[str]", read_line())
    ans = Solution().groupStrings(words)

    print("\noutput:", serialize(ans))
