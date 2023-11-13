# Created by Jones at 2023/11/13 19:12
# leetgo: dev
# https://leetcode.cn/problems/range-sum-query-mutable/

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


class BIT:
    def __init__(self, n: int) -> None:
        self.q = [0] * (n + 1)

    def lowbit(self, x: int):
        return x & -x

    def update(self, x: int, d: int):
        while x < len(self.q):
            self.q[x] += d
            x += self.lowbit(x)

    def query(self, x: int) -> int:
        res = 0
        while x > 0:
            res += self.q[x]
            x -= self.lowbit(x)
        return res


class NumArray:
    def __init__(self, nums: List[int]):
        n = len(nums)
        bit = BIT(n)
        for i, x in enumerate(nums, 1):
            bit.update(i, x)
        self.bit = bit

    def update(self, index: int, val: int) -> None:
        pre = self.bit.query(index + 1) - self.bit.query(index)
        self.bit.update(index + 1, val - pre)

    def sumRange(self, left: int, right: int) -> int:
        return self.bit.query(right + 1) - self.bit.query(left)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    constructor_params = split_array(params[0])
    nums: List[int] = deserialize("List[int]", constructor_params[0])
    obj = NumArray(nums)

    for i in range(1, len(ops)):
        match ops[i]:
            case "update":
                method_params = split_array(params[i])
                index: int = deserialize("int", method_params[0])
                val: int = deserialize("int", method_params[1])
                obj.update(index, val)
                output.append("null")
            case "sumRange":
                method_params = split_array(params[i])
                left: int = deserialize("int", method_params[0])
                right: int = deserialize("int", method_params[1])
                ans = serialize(obj.sumRange(left, right))
                output.append(ans)

    print("\noutput:", join_array(output))
