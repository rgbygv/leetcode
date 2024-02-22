# Created by Jones at 2024/02/22 13:22
# leetgo: 1.4.1
# https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-postorder-traversal/

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
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        # find root
        v = preorder[0]
        postorder.pop()
        root = TreeNode(v)
        if len(preorder)==1:
            return root
        # find left
        left = preorder[1]
        size = postorder.index(left) # 0..=size is left

        root.left = self.constructFromPrePost(preorder[1:1+1+size], postorder[:size+1])
        root.right = self.constructFromPrePost(preorder[1+1+size:], postorder[size+1:])
        return root
        
        

# @lc code=end

if __name__ == "__main__":
    preorder: List[int] = deserialize("List[int]", read_line())
    postorder: List[int] = deserialize("List[int]", read_line())
    ans = Solution().constructFromPrePost(preorder, postorder)
    print("\noutput:", serialize(ans, "TreeNode"))
