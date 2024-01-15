# Created by Jones at 2024/01/15 12:23
# leetgo: dev
# https://leetcode.cn/problems/remove-duplicates-from-sorted-list-ii/

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

        dummy = ListNode(next=head)
        cur = dummy
        while cur.next:
            p = cur.next
            ok = True
            while p.next and p.next.val == p.val:
                ok = False
                p.next = p.next.next
            if ok:
                p = p.next
                cur = cur.next
            else:
                cur.next = p.next
                
            # print(cur.val, p.val)
        return dummy.next


# @lc code=end

if __name__ == "__main__":
    head: ListNode = deserialize("ListNode", read_line())
    ans = Solution().deleteDuplicates(head)

    print("\noutput:", serialize(ans))
