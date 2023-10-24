# Created by Jones at 2023/10/24 16:30
# leetgo: dev
# https://leetcode.cn/problems/find-largest-value-in-each-tree-row/

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


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []

        q = deque([root])

        while q:
            n = len(q)
            cur = -inf
            for _ in range(n):
                x = q.popleft()
                if x.val > cur:
                    cur = x.val
                if x.left:
                    q.append(x.left)
                if x.right:
                    q.append(x.right)

            res.append(cur)
        return res


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().largestValues(root)

    print("\noutput:", serialize(ans))
