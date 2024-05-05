# Created by Jones at 2024/05/05 15:39
# leetgo: 1.4.6
# https://leetcode.com/problems/delete-node-in-a-linked-list/

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

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next


# @lc code=end

# Warning: this is a manual question, the generated test code may be incorrect.
# if __name__ == "__main__":
#     head: ListNode = deserialize("ListNode", read_line())
#     node: int = deserialize("int", read_line())
#     Solution().deleteNode(node)
#     ans = head
#     print("\noutput:", serialize(ans, "ListNode"))
