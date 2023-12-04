# Created by Jones at 2023/12/04 13:34
# leetgo: dev
# https://leetcode.cn/problems/binary-search-tree-to-greater-sum-tree/

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
from string import ascii_lowercase
from typing import List, Optional

# @lc code=begin
# from sortedcontainers import SortedList


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def dfs(root, up=0):
            if not root:
                return 0
            # pre = root.val
            root.val += up
            right = dfs(root.right, up)
            root.val += right
            left = dfs(root.left, root.val)
            # print(pre, root.val, up)
            return root.val + left - up

        dfs(root)

        return root


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().bstToGst(root)

    print("\noutput:", serialize(ans))
