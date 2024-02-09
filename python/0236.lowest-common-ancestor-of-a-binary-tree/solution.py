# Created by Jones at 2024/02/09 13:21
# leetgo: 1.4.1
# https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/

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
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        depth = {}
        fa = defaultdict(lambda:inf)
        mp = {}
        def dfs(root, d):
            if not root:
                return
            # val -> root
            mp[root.val] = root
            depth[root.val] = d
            if root.left:
                fa[root.left.val] = root.val
                dfs(root.left, d+1)
            if root.right:
                fa[root.right.val] = root.val
                dfs(root.right, d+1)
        
        dfs(root, 0)
        
        
        # fa of fa
        N = (int(1e5)+1).bit_length()
        pp = [defaultdict(lambda:inf) for _ in range(N)]
        pp[0] = fa
        # print(fa)
        for i in range(1,N):
            for x in mp:
                y = pp[i-1][x]
                if y != inf:
                    pp[i][x] = pp[i-1][y]

        # make p, q in the same depth
        x, y = p.val, q.val
        if depth[x] > depth[y]:
            x,y = y, x
        k = depth[y] - depth[x]
        for i in range(N):
            if k >> i & 1:
                y = pp[i][y]
        
                
        if x != y:
            for i in range(N-1,-1,-1):
                px,py = pp[i][x], pp[i][y]
                if px != py:
                    x, y = px, py
            # print(x,y)
            x = pp[0][x]
        

        return mp[x]
                    
                
            



            
        

# @lc code=end

# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    p: int = deserialize("int", read_line())
    q: int = deserialize("int", read_line())
    ans = Solution().lowestCommonAncestor(root, p, q)
    print("\noutput:", serialize(ans, "TreeNode"))
