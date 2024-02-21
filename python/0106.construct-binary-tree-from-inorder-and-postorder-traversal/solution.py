# Created by Jones at 2024/02/21 12:34
# leetgo: 1.4.1
# https://leetcode.cn/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

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
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        mp = {v: i for i, v in enumerate(inorder)}

        def dfs(l: int, r: int, L: int, R: int):
            assert r - l == R - L
            if l == r:
                return TreeNode(postorder[r])
            if l > r:
                return None
            # find the root
            val = postorder[r]
            root = TreeNode(val)
            # find left
            i = mp[val]  # L .. i is left
            left_size = i - L
            root.left = dfs(l, l + left_size - 1, L, i - 1)
            root.right = dfs(l + left_size, r - 1, i + 1, R)
            return root

        n = len(inorder) 
        return dfs(0, n - 1, 0, n - 1)


# @lc code=end

if __name__ == "__main__":
    inorder: List[int] = deserialize("List[int]", read_line())
    postorder: List[int] = deserialize("List[int]", read_line())
    ans = Solution().buildTree(inorder, postorder)
    print("\noutput:", serialize(ans, "TreeNode"))
