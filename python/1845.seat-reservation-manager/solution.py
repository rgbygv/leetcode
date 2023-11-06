# Created by Jones at 2023/11/06 14:40
# leetgo: dev
# https://leetcode.cn/problems/seat-reservation-manager/

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


class SeatManager:
    def __init__(self, n: int):
        self.q = list(range(1, n + 1))
        heapify(self.q)

    def reserve(self) -> int:
        return heappop(self.q)

    def unreserve(self, seatNumber: int) -> None:
        heappush(self.q, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    constructor_params = split_array(params[0])
    n: int = deserialize("int", constructor_params[0])
    obj = SeatManager(n)

    for i in range(1, len(ops)):
        match ops[i]:
            case "reserve":
                ans = serialize(obj.reserve())
                output.append(ans)
            case "unreserve":
                method_params = split_array(params[i])
                seatNumber: int = deserialize("int", method_params[0])
                obj.unreserve(seatNumber)
                output.append("null")

    print("\noutput:", join_array(output))
