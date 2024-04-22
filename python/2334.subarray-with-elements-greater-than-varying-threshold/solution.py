# Created by Jones at 2024/04/22 14:31
# leetgo: 1.4.5
# https://leetcode.cn/problems/subarray-with-elements-greater-than-varying-threshold/

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
# from sortedcontainers import SortedList


# class ContinuousLength:
#     def __init__(self) -> None:
#         self.q = SortedList()
#         self.last = 0  # cache the last result

#     def add(self, x: int) -> int:
#         """return the max length of continue segment


#         we can impl it by insert [x,x] and use binary_search to
#         """
class UnionFind:
    def __init__(self, n) -> None:
        self.components = n
        self.fa = list(range(n))
        self.rank = [1] * n

    def __str__(self) -> str:
        return " ".join(map(str, self.fa))

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
        self.components -= 1
        return True

    def merge(self, x, y):
        fx, fy = self.find(x), self.find(y)
        self.rank[fy] += self.rank[fx]
        self.fa[fx] = fy

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)

    def all_is_connected(self):
        return self.components == 1

    def size(self, x):
        return self.rank[self.find(x)]


class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        if max(nums) > threshold:
            return 1

        n = len(nums)
        uf = UnionFind(n)
        s = set()
        mp = [(v, i) for i, v in enumerate(nums)]

        for x, i in sorted(mp, reverse=True):
            # we add x to a datastruct
            # if we find a continue segment whose size * x > threshold
            # we can return that size
            s.add(i)
            if i + 1 in s:
                uf.union(i + 1, i)

            if i - 1 in s:
                uf.union(i - 1, i)

            size = uf.size(i)
            # print(x, i, size)
            if size * x > threshold:
                return size
        return -1


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    threshold: int = deserialize("int", read_line())
    ans = Solution().validSubarraySize(nums, threshold)
    print("\noutput:", serialize(ans, "integer"))
