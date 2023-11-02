# Created by Jones at 2023/11/02 13:56
# leetgo: dev
# https://leetcode.cn/problems/count-nodes-equal-to-average-of-subtree/

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
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root):
            nonlocal res
            if not root:
                return 0, 0
            left, cnt1 = dfs(root.left)
            right, cnt2 = dfs(root.right)

            cur, cur_cnt = left + right + root.val, cnt1 + cnt2 + 1
            if root.val == cur // cur_cnt:
                res += 1

            return cur, cur_cnt

        dfs(root)

        return res


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().averageOfSubtree(root)

    print("\noutput:", serialize(ans))
