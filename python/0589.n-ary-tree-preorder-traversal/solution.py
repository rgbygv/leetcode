# Created by Jones at 2024/02/18 12:25
# leetgo: 1.4.1
# https://leetcode.cn/problems/n-ary-tree-preorder-traversal/

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

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: "Node") -> List[int]:
        res = []

        def dfs(root):
            if not root:
                return
            res.append(root.val)
            for child in root.children:
                dfs(child)

        dfs(root)
        return res


# @lc code=end

# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    root: int = deserialize("int", read_line())
    ans = Solution().preorder(root)
    print("\noutput:", serialize(ans, "integer[]"))
