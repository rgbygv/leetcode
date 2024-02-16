# Created by Jones at 2024/02/16 12:40
# leetgo: 1.4.1
# https://leetcode.cn/problems/binary-tree-zigzag-level-order-traversal/

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
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque([root])
        res = []
        flg = True # from left to right
        while q:
            cur = []
            n = len(q)
            for _ in range(n):
                root = q.popleft()
                cur.append(root.val)
                if root.left:
                    q.append(root.left)
                if root.right:
                    q.append(root.right)
            if flg:
                res.append(cur)
            else:
                res.append(cur[::-1])
            flg = not flg
        return res
            

            
        

# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().zigzagLevelOrder(root)
    print("\noutput:", serialize(ans, "integer[][]"))
