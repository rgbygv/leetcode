# Created by Jones at 2024/01/14 14:28
# leetgo: dev
# https://leetcode.cn/problems/remove-duplicates-from-sorted-list/

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


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        # nxt = self.deleteDuplicates(head.next)
        # if nxt and head.val == nxt.val:
        #     return nxt
        # head.next = nxt
        # return head
        dummp = ListNode(0)
        p = dummp
        while head:
            nxt = head.next
            while nxt and nxt.val == head.val:
                nxt = nxt.next
            p.next = head
            head = nxt
            p = p.next
        p.next = head
        return dummp.next


# @lc code=end

if __name__ == "__main__":
    head: ListNode = deserialize("ListNode", read_line())
    ans = Solution().deleteDuplicates(head)

    print("\noutput:", serialize(ans))
