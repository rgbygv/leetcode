# Created by Jones at 2024/02/07 19:58
# leetgo: 1.4.1
# https://leetcode.cn/problems/cousins-in-binary-tree-ii/

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
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        depth = defaultdict(int) # sum of each depth
        def dfs(root, d:int):
            if not root:
                return
            depth[d] += root.val
            dfs(root.left, d+1)
            dfs(root.right, d+1)
            if root.left and root.right:
                x,y = root.left.val, root.right.val
                root.left.val = root.right.val = x + y
        
        dfs(root, 0)
        # print(depth)
        
        def change(root, d:int):
            if not root:
                return 
            root.val = depth[d] - root.val
            change(root.left, d+1)
            change(root.right, d+1)
            
        change(root,0)
        
        return root
                

# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().replaceValueInTree(root)
    print("\noutput:", serialize(ans, "TreeNode"))
