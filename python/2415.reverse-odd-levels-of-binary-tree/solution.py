# Created by Jones at 2023/12/15 16:04
# leetgo: dev
# https://leetcode.cn/problems/reverse-odd-levels-of-binary-tree/

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
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        q = deque([root])
        flg = False
        while q:
            n = len(q)
            if flg:
                for i in range(n >> 1):
                    q[i].val, q[n - 1 - i].val = q[n - 1 - i].val, q[i].val

            for _ in range(n):
                node = q.popleft()
                if node.left:  # perfect tree
                    q.append(node.left)
                    q.append(node.right)

            flg = not flg
        return root


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().reverseOddLevels(root)

    print("\noutput:", serialize(ans))
