# Created by Jones at 2024/05/18 08:25
# leetgo: 1.4.7
# https://leetcode.com/problems/distribute-coins-in-binary-tree/

from typing import *
from leetgo_py import *

from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from functools import cache, cmp_to_key, lru_cache, reduce
from heapq import heapify, heappop, heappush, heappushpop, heapreplace
from icecream import ic
from itertools import accumulate, chain, count, pairwise, zip_longest
from math import ceil, comb, floor, gcd, inf, isqrt, lcm, log2, perm, sqrt
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
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root):
            nonlocal res
            if not root:
                return 0
            need = dfs(root.left) + dfs(root.right)
            root.val += need - 1
            res += abs(root.val)
            return root.val

        dfs(root)
        return res


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().distributeCoins(root)
    print("\noutput:", serialize(ans, "integer"))
