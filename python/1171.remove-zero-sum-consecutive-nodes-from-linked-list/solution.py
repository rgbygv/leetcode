# Created by Jones at 2024/03/12 12:21
# leetgo: 1.4.2
# https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/

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


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        mp = {0: dummy}

        p = head
        s = 0
        while p:
            s += p.val
            if s in mp:
                pre = mp[s]
                # print(p.val, s, pre.val)

                tmp = pre.next
                ss = s
                while tmp is not p:
                    ss += tmp.val
                    del mp[ss]
                    tmp = tmp.next

                pre.next = p.next
            else:
                mp[s] = p
            p = p.next

        return dummy.next


# @lc code=end

if __name__ == "__main__":
    head: ListNode = deserialize("ListNode", read_line())
    ans = Solution().removeZeroSumSublists(head)
    print("\noutput:", serialize(ans, "ListNode"))
