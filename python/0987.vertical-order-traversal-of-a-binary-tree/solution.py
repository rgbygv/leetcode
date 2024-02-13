# Created by Jones at 2024/02/13 17:49
# leetgo: 1.4.1
# https://leetcode.cn/problems/vertical-order-traversal-of-a-binary-tree/

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
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        mp = defaultdict(list)
        def dfs(root, x, y):
            if not root:
                return
            mp[y].append((x,root.val))
            dfs(root.left, x+1,y-1)
            dfs(root.right, x+1,y+1)
        
        dfs(root, 0, 0)
        
        res = []
        
        for y in sorted(mp.keys()):
            mp[y].sort()
            res.append([v for _,v  in mp[y]])

        return res



# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().verticalTraversal(root)
    print("\noutput:", serialize(ans, "integer[][]"))
