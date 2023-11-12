# Created by Jones at 2023/11/12 10:30
# leetgo: dev
# https://leetcode.cn/problems/maximum-strong-pair-xor-ii/
# https://leetcode.cn/contest/weekly-contest-371/problems/maximum-strong-pair-xor-ii/

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


class Node:
    __slots__ = "children", "cnt"

    def __init__(self):
        self.children = [None, None]
        self.cnt = 0  # 子树大小


class Trie:
    HIGH_BIT = 19

    def __init__(self):
        self.root = Node()

    # 添加 val
    def insert(self, val: int) -> None:
        cur = self.root
        for i in range(Trie.HIGH_BIT, -1, -1):
            bit = (val >> i) & 1
            if cur.children[bit] is None:
                cur.children[bit] = Node()
            cur = cur.children[bit]
            cur.cnt += 1  # 维护子树大小
        return cur

    # 删除 val，但不删除节点
    # 要求 val 必须在 trie 中
    def remove(self, val: int) -> None:
        cur = self.root
        for i in range(Trie.HIGH_BIT, -1, -1):
            cur = cur.children[(val >> i) & 1]
            cur.cnt -= 1  # 维护子树大小
        return cur

    # 返回 val 与 trie 中一个元素的最大异或和
    # 要求 trie 中至少有一个元素
    def max_xor(self, val: int) -> int:
        cur = self.root
        ans = 0
        for i in range(Trie.HIGH_BIT, -1, -1):
            bit = (val >> i) & 1
            # 如果 cur.children[bit^1].cnt == 0，视作空节点
            if cur.children[bit ^ 1] and cur.children[bit ^ 1].cnt:
                ans |= 1 << i
                bit ^= 1
            cur = cur.children[bit]
        return ans


class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        # `|x - y| <= min(x, y)`
        # assume x < y => y - x <= x
        # x < y <= 2x
        nums = sorted(set(nums))
        res = 0
        l = 0
        trie = Trie()
        for _, y in enumerate(nums):
            while nums[l] * 2 < y:
                trie.remove(nums[l])
                l += 1
            trie.insert(y)
            res = max(res, trie.max_xor(y))
        return res


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maximumStrongPairXor(nums)

    print("\noutput:", serialize(ans))
