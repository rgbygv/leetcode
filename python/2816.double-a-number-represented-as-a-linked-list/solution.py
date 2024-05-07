# Created by Jones at 2024/05/07 12:55
# leetgo: 1.4.6
# https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/

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
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        1 -> 7 -> 8
        reverse it, then double it, then reverse back
        but i don't want do it
        """

        st = []
        while head:
            st.append(head)
            head = head.next

        st.reverse()
        carry = 0
        for node in st:
            carry += node.val * 2
            node.val = carry % 10
            carry //= 10

        if carry:
            new_head = ListNode(carry, st[-1])
            return new_head

        return st[-1]


# @lc code=end

if __name__ == "__main__":
    head: ListNode = deserialize("ListNode", read_line())
    ans = Solution().doubleIt(head)
    print("\noutput:", serialize(ans, "ListNode"))
