# Created by Jones at 2024/02/23 13:05
# leetgo: 1.4.1
# https://leetcode.cn/problems/kth-largest-sum-in-a-binary-tree/

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
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1
        q = deque([root])
        s = []
        while q:
            n = len(q)
            cur = 0
            for _ in range(n):
                root = q.popleft()
                cur += root.val
                for node in (root.left, root.right):
                    if node:
                        q.append(node)
            s.append(cur)
        if len(s) < k:
            return -1
        k -= 1
        s.sort(reverse=1)
        return s[k]


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().kthLargestLevelSum(root, k)
    print("\noutput:", serialize(ans, "long"))
