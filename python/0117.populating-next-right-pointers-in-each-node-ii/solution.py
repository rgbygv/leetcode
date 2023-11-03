# Created by Jones at 2023/11/03 20:15
# leetgo: dev
# https://leetcode.cn/problems/populating-next-right-pointers-in-each-node-ii/

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

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: "Node") -> "Node":
        if not root:
            return root

        ori = root
        q = deque([root])

        while q:
            n = len(q)
            for i in range(n):
                root = q.popleft()
                if i != n - 1:
                    root.next = q[0]
                if root.left:
                    q.append(root.left)
                if root.right:
                    q.append(root.right)
        return ori


# @lc code=end

# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().connect(root)

    print("\noutput:", serialize(ans))
