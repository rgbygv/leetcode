# Created by Bob at 2024/01/06 13:02
# leetgo: dev
# https://leetcode.cn/problems/insert-greatest-common-divisors-in-linked-list/

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
    def insertGreatestCommonDivisors(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not head.next:
            return head
        node = self.insertGreatestCommonDivisors(head.next)

        g = gcd(head.val, node.val)

        cur = ListNode(g, node)
        head.next = cur
        return head


# @lc code=end

if __name__ == "__main__":
    head: ListNode = deserialize("ListNode", read_line())
    ans = Solution().insertGreatestCommonDivisors(head)

    print("\noutput:", serialize(ans))
