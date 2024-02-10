# Created by Jones at 2024/02/10 09:54
# leetgo: 1.4.1
# https://leetcode.cn/problems/binary-tree-inorder-traversal/

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
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        # def dfs(root):
        #     if not root:
        #         return
        #     dfs(root.left)
        #     q.append(root.val)
        #     dfs(root.right)
        
        q = []
        st = [root]
        while st:
            root = st.pop()
            if not root:continue
            if root.left:
                st.append(root)
                st.append(root.left)
                root.left = None
                continue
            q.append(root.val)
            if root.right:
                st.append(root.right)
        
        return q
            
        return q

# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().inorderTraversal(root)
    print("\noutput:", serialize(ans, "integer[]"))
