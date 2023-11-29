# Created by Jones at 2023/11/29 12:24
# leetgo: dev
# https://leetcode.cn/problems/smallest-number-in-infinite-set/

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


class SmallestInfiniteSet:
    def __init__(self):
        self.s = set()
        self.q = list(range(1, 1001))

    def popSmallest(self) -> int:
        x = heappop(self.q)
        self.s.add(x)
        return x

    def addBack(self, num: int) -> None:
        if num in self.s:
            heappush(self.q, num)
            self.s.remove(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    obj = SmallestInfiniteSet()

    for i in range(1, len(ops)):
        match ops[i]:
            case "popSmallest":
                ans = serialize(obj.popSmallest())
                output.append(ans)
            case "addBack":
                method_params = split_array(params[i])
                num: int = deserialize("int", method_params[0])
                obj.addBack(num)
                output.append("null")

    print("\noutput:", join_array(output))
