# Created by Jones at 2024/04/14 12:56
# leetgo: 1.4.5
# https://leetcode.com/problems/sum-of-left-leaves/

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
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root, is_left: bool):
            if not root:
                return
            nonlocal res
            if is_left and not root.left and not root.right:
                res += root.val
            dfs(root.left, True)
            dfs(root.right, False)

        dfs(root, False)
        return res


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().sumOfLeftLeaves(root)
    print("\noutput:", serialize(ans, "integer"))
