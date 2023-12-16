# Created by Jones at 2023/12/16 19:10
# leetgo: dev
# https://leetcode.cn/problems/count-integers-in-intervals/

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


class CountIntervals:
    __slots__ = "left", "right", "l", "r", "cnt"

    def __init__(self, l=1, r=10**9):
        self.left = self.right = None
        self.l, self.r, self.cnt = l, r, 0

    def add(self, l: int, r: int) -> None:
        if self.cnt == self.r - self.l + 1:
            return
        if l <= self.l and self.r <= r:
            self.cnt = self.r - self.l + 1
            return

        mid = (self.l + self.r) // 2
        if self.left is None:
            self.left = CountIntervals(self.l, mid)
        if self.right is None:
            self.right = CountIntervals(mid + 1, self.r)
        if l <= mid:
            self.left.add(l, r)
        if mid < r:
            self.right.add(l, r)
        self.cnt = self.left.cnt + self.right.cnt

    def count(self) -> int:
        return self.cnt


# Your CountIntervals object will be instantiated and called as such:
# obj = CountIntervals()
# obj.add(left,right)
# param_2 = obj.count()

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    obj = CountIntervals()

    for i in range(1, len(ops)):
        match ops[i]:
            case "add":
                method_params = split_array(params[i])
                left: int = deserialize("int", method_params[0])
                right: int = deserialize("int", method_params[1])
                obj.add(left, right)
                output.append("null")
            case "count":
                ans = serialize(obj.count())
                output.append(ans)

    print("\noutput:", join_array(output))
