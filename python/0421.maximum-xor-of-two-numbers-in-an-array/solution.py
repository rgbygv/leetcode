# Created by Jones at 2023/11/04 14:12
# leetgo: dev
# https://leetcode.cn/problems/maximum-xor-of-two-numbers-in-an-array/

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


class Trie:
    L = 31

    def __init__(self):
        self.left = self.right = None

    def insert(self, x):
        node = self
        for i in range(Trie.L)[::-1]:
            bit = x >> i & 1
            if bit == 0:
                if not node.left:
                    node.left = Trie()
                node = node.left
            else:
                if not node.right:
                    node.right = Trie()
                node = node.right

    def search(self, x):
        res = 0
        node = self
        for i in range(Trie.L)[::-1]:
            bit = x >> i & 1
            check = False
            if bit == 0:
                if node.right:
                    node = node.right
                    check = True
                else:
                    node = node.left
            else:
                if node.left:
                    node = node.left
                    check = True
                else:
                    node = node.right
            if check:
                res |= 1 << i
        return res


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = Trie()
        res = 0
        for x in sorted(nums, reverse=True):
            trie.insert(x)
            res = max(res, trie.search(x))
        return res


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().findMaximumXOR(nums)

    print("\noutput:", serialize(ans))
