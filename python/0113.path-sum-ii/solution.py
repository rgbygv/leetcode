# Created by Jones at 2023/12/18 21:52
# leetgo: dev
# https://leetcode.cn/problems/path-sum-ii/

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
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []

        res = []
        path = []

        def dfs(root, target: int):
            if not root:
                return
            path.append(root.val)
            if not root.left and not root.right:
                if root.val == target:
                    res.append(path[:])
            else:
                dfs(root.left, target - root.val)
                dfs(root.right, target - root.val)
            path.pop()

        dfs(root, targetSum)

        return res


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    targetSum: int = deserialize("int", read_line())
    ans = Solution().pathSum(root, targetSum)

    print("\noutput:", serialize(ans))
