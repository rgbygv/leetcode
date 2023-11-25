# Created by Jones at 2023/11/25 13:40
# leetgo: dev
# https://leetcode.cn/problems/pseudo-palindromic-paths-in-a-binary-tree/

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
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        cnt = [0] * 10
        res = 0

        def dfs(o):
            if not o:
                return
            nonlocal res
            cnt[o.val] += 1
            if not o.left and not o.right:
                res += sum(x & 1 for x in cnt) <= 1
            else:
                dfs(o.left)
                dfs(o.right)
            cnt[o.val] -= 1

        dfs(root)

        return res


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().pseudoPalindromicPaths(root)

    print("\noutput:", serialize(ans))
