# Created by Jones at 2024/02/25 12:48
# leetgo: 1.4.1
# https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-search-tree/

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
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        # we can know p <= lca <= q
        if p.val > q.val:
            p, q = q, p
        if root.val < p.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        return root


# @lc code=end

# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    p: int = deserialize("int", read_line())
    q: int = deserialize("int", read_line())
    ans = Solution().lowestCommonAncestor(root, p, q)
    print("\noutput:", serialize(ans, "TreeNode"))
