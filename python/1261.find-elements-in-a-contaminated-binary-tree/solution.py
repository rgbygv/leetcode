# Created by Jones at 2024/03/12 11:56
# leetgo: 1.4.2
# https://leetcode.cn/problems/find-elements-in-a-contaminated-binary-tree/

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
class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        self.seen = set()

        def dfs(root, val):
            if not root:
                return
            root.val = val
            self.seen.add(val)
            dfs(root.left, val * 2 + 1)
            dfs(root.right, val * 2 + 2)
            return root

        self.root = dfs(root, 0)

    def find(self, target: int) -> bool:
        return target in self.seen
        # def dfs(root, target):
        #     if not root:
        #         return False
        #     if root.val == target:
        #         return True
        #     if root.val * 2 >= target:
        #         return False
        #     return dfs(root.left, target) or dfs(root.right, target)

        # return dfs(self.root, target)


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    constructor_params = split_array(params[0])
    root: TreeNode = deserialize("TreeNode", constructor_params[0])
    obj = FindElements(root)

    for i in range(1, len(ops)):
        match ops[i]:
            case "find":
                method_params = split_array(params[i])
                target: int = deserialize("int", method_params[0])
                ans = serialize(obj.find(target))
                output.append(ans)

    print("\noutput:", join_array(output))
