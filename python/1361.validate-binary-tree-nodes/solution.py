# Created by Jones at 2023/10/17 11:29
# leetgo: dev
# https://leetcode.cn/problems/validate-binary-tree-nodes/

from typing import *
from leetgo_py import *

# import sys

# sys.path.append("..")
# from _LEETCODE import *

# @lc code=begin
# from sortedcontainers import SortedList


class Solution:
    def validateBinaryTreeNodes(
        self, n: int, leftChild: List[int], rightChild: List[int]
    ) -> bool:
        # find root
        deg = [0] * n
        for left, right in zip(leftChild, rightChild):
            if left != -1:
                deg[left] += 1
            if right != -1:
                deg[right] += 1

        root = [i for i, d in enumerate(deg) if d == 0]

        if len(root) != 1:
            return False

        root = root[0]
        vis = [0] * n

        def dfs(root):
            vis[root] += 1
            if vis[root] > 1:
                return
            l = leftChild[root]
            if l != -1:
                dfs(l)
            r = rightChild[root]
            if r != -1:
                dfs(r)

        dfs(root)

        return all(x == 1 for x in vis)


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    leftChild: List[int] = deserialize("List[int]", read_line())
    rightChild: List[int] = deserialize("List[int]", read_line())
    ans = Solution().validateBinaryTreeNodes(n, leftChild, rightChild)

    print("\noutput:", serialize(ans))
