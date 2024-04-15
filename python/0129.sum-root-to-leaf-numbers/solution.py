# Created by Jones at 2024/04/15 11:45
# leetgo: 1.4.5
# https://leetcode.com/problems/sum-root-to-leaf-numbers/

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
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root, x: int):
            if not root:
                return
            x = x * 10 + root.val
            if not root.left and not root.right:
                nonlocal res
                res += x
            dfs(root.left, x)
            dfs(root.right, x)

        dfs(root, 0)
        return res


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().sumNumbers(root)
    print("\noutput:", serialize(ans, "integer"))
