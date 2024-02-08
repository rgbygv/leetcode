# Created by Jones at 2024/02/08 11:54
# leetgo: 1.4.1
# https://leetcode.cn/problems/cousins-in-binary-tree/

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
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        N = 101
        depth = [0] * N
        fa = [-1] * N
        
        def dfs(root, d):
            if not root:
                return
            depth[root.val] = d
            if root.left:
                fa[root.left.val] = root.val
                dfs(root.left, d+1)
            if root.right:
                fa[root.right.val] =root.val
                dfs(root.right, d+1)
        
        dfs(root, 0)
        
        return depth[x] == depth[y] and fa[x] != fa[y]

# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    x: int = deserialize("int", read_line())
    y: int = deserialize("int", read_line())
    ans = Solution().isCousins(root, x, y)
    print("\noutput:", serialize(ans, "boolean"))
