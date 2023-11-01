# Created by Jones at 2023/11/01 20:52
# leetgo: dev
# https://leetcode.cn/problems/find-mode-in-binary-search-tree/

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
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        cnt = Counter()

        def dfs(root):
            if not root:
                return
            cnt[root.val] += 1
            dfs(root.left)
            dfs(root.right)

        dfs(root)

        mx = max(cnt.values())

        return [i for i, v in cnt.items() if v == mx]


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().findMode(root)

    print("\noutput:", serialize(ans))
