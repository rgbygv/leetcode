# Created by Jones at 2024/04/24 09:21
# leetgo: 1.4.5
# https://leetcode.cn/problems/amount-of-time-for-binary-tree-to-be-infected/

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
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        # build graph
        g = defaultdict(list)

        def dfs(root):
            if not root:
                return
            for child in (root.left, root.right):
                if child:
                    g[root.val].append(child.val)
                    g[child.val].append(root.val)
                    dfs(child)

        dfs(root)

        # then bfs, find the minium time
        q = deque([(start, -1)])
        t = -1

        while q:
            n = len(q)
            for _ in range(n):
                x, fa = q.popleft()
                for y in g[x]:
                    if y != fa:
                        q.append((y, x))
            t += 1
        return t


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    start: int = deserialize("int", read_line())
    ans = Solution().amountOfTime(root, start)
    print("\noutput:", serialize(ans, "integer"))
