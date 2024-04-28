# Created by Jones at 2024/04/28 20:07
# leetgo: 1.4.5
# https://leetcode.cn/problems/exam-room/

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
from sortedcontainers import SortedList


class ExamRoom:
    def __init__(self, n: int):
        self.n = n - 1
        self.q = SortedList()

    def seat(self) -> int:
        if not self.q:
            key = 0
        elif len(self.q) == 1:
            x = self.q[0]
            if x >= self.n - x:
                key = 0
            else:
                key = self.n
        else:
            d = 0
            key = -1
            for x, y in pairwise(self.q):
                diff = y - x
                if diff > 1 and diff // 2 > d // 2:
                    d = diff
                    key = x + diff // 2
            # try place `0`
            if 0 != self.q[0]:
                x = -1
                diff = self.q[0] - x
                if diff // 2 >= d // 2:
                    d = diff
                    key = 0

            # try place `n`
            if self.q[-1] != self.n:
                diff = self.n - self.q[-1] + 1
                if diff // 2 > d // 2:
                    d = diff
                    key = self.n

        self.q.add(key)
        # print(self.q)
        return key

    def leave(self, p: int) -> None:
        self.q.remove(p)


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    constructor_params = split_array(params[0])
    n: int = deserialize("int", constructor_params[0])
    obj = ExamRoom(n)

    for i in range(1, len(ops)):
        match ops[i]:
            case "seat":
                ans = serialize(obj.seat())
                output.append(ans)
            case "leave":
                method_params = split_array(params[i])
                p: int = deserialize("int", method_params[0])
                obj.leave(p)
                output.append("null")

    print("\noutput:", join_array(output))
