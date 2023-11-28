# Created by Jones at 2023/11/28 13:24
# leetgo: dev
# https://leetcode.cn/problems/design-front-middle-back-queue/

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


class FrontMiddleBackQueue:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def balance(self):
        #  assert 0 <= len(q2) - len(q1) <= 1
        if len(self.q1) > len(self.q2):
            self.q2.appendleft(self.q1.pop())
        elif len(self.q1) + 1 < len(self.q2):
            self.q1.append(self.q2.popleft())

    def pushFront(self, val: int) -> None:
        self.q1.appendleft(val)
        self.balance()

    def pushMiddle(self, val: int) -> None:
        if len(self.q1) == len(self.q2):
            self.q2.appendleft(val)
        else:
            self.q1.append(val)

    def pushBack(self, val: int) -> None:
        self.q2.append(val)
        self.balance()

    def popFront(self) -> int:
        if not self.q2:
            return -1
        if not self.q1:
            return self.q2.popleft()
        val = self.q1.popleft()
        self.balance()
        return val

    def popMiddle(self) -> int:
        if not self.q2:
            return -1
        if len(self.q1) < len(self.q2):
            return self.q2.popleft()
        return self.q1.pop()

    def popBack(self) -> int:
        if not self.q2:
            return -1
        val = self.q2.pop()
        self.balance()
        return val


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    obj = FrontMiddleBackQueue()

    for i in range(1, len(ops)):
        match ops[i]:
            case "pushFront":
                method_params = split_array(params[i])
                val: int = deserialize("int", method_params[0])
                obj.pushFront(val)
                output.append("null")
            case "pushMiddle":
                method_params = split_array(params[i])
                val: int = deserialize("int", method_params[0])
                obj.pushMiddle(val)
                output.append("null")
            case "pushBack":
                method_params = split_array(params[i])
                val: int = deserialize("int", method_params[0])
                obj.pushBack(val)
                output.append("null")
            case "popFront":
                ans = serialize(obj.popFront())
                output.append(ans)
            case "popMiddle":
                ans = serialize(obj.popMiddle())
                output.append(ans)
            case "popBack":
                ans = serialize(obj.popBack())
                output.append(ans)

    print("\noutput:", join_array(output))
