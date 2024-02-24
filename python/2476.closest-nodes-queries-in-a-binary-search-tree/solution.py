# Created by Jones at 2024/02/24 13:34
# leetgo: 1.4.1
# https://leetcode.cn/problems/closest-nodes-queries-in-a-binary-search-tree/

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
    def closestNodes(
        self, root: Optional[TreeNode], queries: List[int]
    ) -> List[List[int]]:
        q = []

        def dfs(root):
            if not root:
                return
            dfs(root.left)
            q.append(root.val)
            dfs(root.right)

        dfs(root)

        res = []
        for x in queries:
            cur = []
            # find <= x
            i = bisect_right(q, x) - 1
            cur.append(-1 if i < 0 else q[i])
            i = bisect_left(q, x)
            cur.append(-1 if i == len(q) else q[i])
            res.append(cur)
        return res


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    queries: List[int] = deserialize("List[int]", read_line())
    ans = Solution().closestNodes(root, queries)
    print("\noutput:", serialize(ans, "integer[][]"))
