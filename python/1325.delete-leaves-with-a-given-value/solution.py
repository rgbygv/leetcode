# Created by Jones at 2024/05/17 12:40
# leetgo: 1.4.7
# https://leetcode.com/problems/delete-leaves-with-a-given-value/

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


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(
        self, root: Optional[TreeNode], target: int
    ) -> Optional[TreeNode]:
        def dfs(root: Optional[TreeNode]):
            if not root:
                return root
            root.left = dfs(root.left)
            root.right = dfs(root.right)
            if not root.left and not root.right and root.val == target:
                return None
            return root

        return dfs(root)


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().removeLeafNodes(root, target)
    print("\noutput:", serialize(ans, "TreeNode"))
