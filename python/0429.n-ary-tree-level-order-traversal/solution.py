# Created by Jones at 2024/02/17 13:23
# leetgo: 1.4.1
# https://leetcode.cn/problems/n-ary-tree-level-order-traversal/

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
    def levelOrder(self, root: "Node") -> List[List[int]]:
        if not root:
            return []
        res = []
        q = deque([root])
        while q:
            n = len(q)
            cur = []
            for _ in range(n):
                root = q.popleft()
                cur.append(root.val)
                if root.children:
                    q += root.children
            res.append(cur)
        return res


# @lc code=end

# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    root: int = deserialize("int", read_line())
    ans = Solution().levelOrder(root)
    print("\noutput:", serialize(ans, "integer[][]"))
