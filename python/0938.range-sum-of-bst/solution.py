# Created by Jones at 2024/02/26 12:14
# leetgo: 1.4.1
# https://leetcode.cn/problems/range-sum-of-bst/

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
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(root):
            if not root:
                return 0
            res = 0
            if low <= root.val <= high:
                res += root.val
            res += dfs(root.left)
            res += dfs(root.right)
            return res

        return dfs(root)


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    low: int = deserialize("int", read_line())
    high: int = deserialize("int", read_line())
    ans = Solution().rangeSumBST(root, low, high)
    print("\noutput:", serialize(ans, "integer"))
