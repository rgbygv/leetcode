# Created by Jones at 2024/04/17 19:37
# leetgo: 1.4.5
# https://leetcode.com/problems/smallest-string-starting-from-leaf/

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
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        res = []
        path = []

        def dfs(root):
            if not root:
                return
            path.append(root.val)
            if not root.left and not root.right:
                res.append(path[::-1])
            dfs(root.left)
            dfs(root.right)
            path.pop()

        dfs(root)

        return "".join(chr(x + ord("a")) for x in min(res))


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().smallestFromLeaf(root)
    print("\noutput:", serialize(ans, "string"))
