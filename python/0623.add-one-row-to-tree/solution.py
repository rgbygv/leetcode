# Created by Jones at 2024/04/16 15:32
# leetgo: 1.4.5
# https://leetcode.com/problems/add-one-row-to-tree/

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


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(
        self, root: Optional[TreeNode], val: int, depth: int
    ) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root)

        def dfs(root, d):
            if not root:
                return
            if d == depth - 1:
                left = root.left
                root.left = TreeNode(val, left, None)
                right = root.right
                root.right = TreeNode(val, None, right)
                return root
            dfs(root.left, d + 1)
            dfs(root.right, d + 1)
            return root

        return dfs(root, 1)


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    val: int = deserialize("int", read_line())
    depth: int = deserialize("int", read_line())
    ans = Solution().addOneRow(root, val, depth)
    print("\noutput:", serialize(ans, "TreeNode"))
