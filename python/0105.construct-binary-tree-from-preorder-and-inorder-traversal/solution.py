# Created by Jones at 2024/02/20 17:00
# leetgo: 1.4.1
# https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # quick get pos
        if not preorder:
            return None
        mp = {v: i for i, v in enumerate(inorder)}
        v = preorder[0]
        root = TreeNode(v)
        i = mp[v]
        root.left = self.buildTree(preorder[1 : i + 1], inorder[:i])
        root.right = self.buildTree(preorder[i + 1 :], inorder[i + 1 :])
        return root


# @lc code=end

if __name__ == "__main__":
    preorder: List[int] = deserialize("List[int]", read_line())
    inorder: List[int] = deserialize("List[int]", read_line())
    ans = Solution().buildTree(preorder, inorder)
    print("\noutput:", serialize(ans, "TreeNode"))
