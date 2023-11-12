# Created by Jones at 2023/11/12 11:52
# leetgo: dev
# https://leetcode.cn/problems/range-module/

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


class Node:
    def __init__(self) -> None:
        self.ls = self.rs = None
        self.val = self.add = False


class SegmentTree:
    def __init__(self):
        self.root = Node()

    @staticmethod
    def update(node: Node, lc: int, rc: int, l: int, r: int, v: bool) -> None:
        if l <= lc and rc <= r:
            node.val = v
            # 注意产生变化懒标记就为True，因为更新有删除
            node.add = True
            return
        SegmentTree.pushdown(node)
        mid = (lc + rc) >> 1
        if l <= mid:
            SegmentTree.update(node.ls, lc, mid, l, r, v)
        if r > mid:
            SegmentTree.update(node.rs, mid + 1, rc, l, r, v)
        SegmentTree.pushup(node)

    @staticmethod
    def query(node: Node, lc: int, rc: int, l: int, r: int) -> bool:
        if l <= lc and rc <= r:
            return node.val
        # 先确保所有关联的懒标记下沉下去
        SegmentTree.pushdown(node)
        mid, ans = (lc + rc) >> 1, True
        if l <= mid:
            ans = ans and SegmentTree.query(node.ls, lc, mid, l, r)
        if r > mid:
            # 同样为不同题目中的更新方式
            ans = ans and SegmentTree.query(node.rs, mid + 1, rc, l, r)
        return ans

    @staticmethod
    def pushdown(node: Node) -> None:
        # 懒标记, 在需要的时候才开拓节点和赋值
        if node.ls is None:
            node.ls = Node()
        if node.rs is None:
            node.rs = Node()
        if not node.add:
            return
        node.ls.val, node.rs.val = node.val, node.val
        # 注意产生变化懒标记就为True，因为更新有删除
        node.ls.add, node.rs.add = True, True
        node.add = False

    @staticmethod
    def pushup(node: Node) -> None:
        # 动态更新方式：此处为两者都true
        node.val = node.ls.val and node.rs.val


N = 10**9 + 1


class RangeModule:
    def __init__(self):
        self.tree = SegmentTree()

    def addRange(self, left: int, right: int) -> None:
        self.tree.update(self.tree.root, 1, N, left, right - 1, True)

    def queryRange(self, left: int, right: int) -> bool:
        return self.tree.query(self.tree.root, 1, N, left, right - 1)

    def removeRange(self, left: int, right: int) -> None:
        self.tree.update(self.tree.root, 1, N, left, right - 1, False)


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    obj = RangeModule()

    for i in range(1, len(ops)):
        match ops[i]:
            case "addRange":
                method_params = split_array(params[i])
                left: int = deserialize("int", method_params[0])
                right: int = deserialize("int", method_params[1])
                obj.addRange(left, right)
                output.append("null")
            case "queryRange":
                method_params = split_array(params[i])
                left: int = deserialize("int", method_params[0])
                right: int = deserialize("int", method_params[1])
                ans = serialize(obj.queryRange(left, right))
                output.append(ans)
            case "removeRange":
                method_params = split_array(params[i])
                left: int = deserialize("int", method_params[0])
                right: int = deserialize("int", method_params[1])
                obj.removeRange(left, right)
                output.append("null")

    print("\noutput:", join_array(output))
