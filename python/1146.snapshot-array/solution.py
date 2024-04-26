# Created by Jones at 2024/04/26 13:19
# leetgo: 1.4.5
# https://leetcode.cn/problems/snapshot-array/

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


class SnapshotArray:
    def __init__(self, length: int):
        self.q = [[(0, 0)] for _ in range(length)]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        snap_id, _ = self.q[index][-1]
        if snap_id == self.snap_id:
            self.q[index][-1] = (snap_id, val)
        else:
            self.q[index].append((self.snap_id, val))

    def snap(self) -> int:
        """if we store self.q in each `snap`, it's bad
        so we should store (val, snap_id) in self.q
        """
        snap_id = self.snap_id
        self.snap_id += 1
        return snap_id

    def get(self, index: int, snap_id: int) -> int:
        """we can use binary search in self.q[index]"""
        v = self.q[index]

        j = bisect_right(v, snap_id, key=lambda e: e[0])
        return v[j - 1][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    constructor_params = split_array(params[0])
    length: int = deserialize("int", constructor_params[0])
    obj = SnapshotArray(length)

    for i in range(1, len(ops)):
        match ops[i]:
            case "set":
                method_params = split_array(params[i])
                index: int = deserialize("int", method_params[0])
                val: int = deserialize("int", method_params[1])
                obj.set(index, val)
                output.append("null")
            case "snap":
                ans = serialize(obj.snap())
                output.append(ans)
            case "get":
                method_params = split_array(params[i])
                index: int = deserialize("int", method_params[0])
                snap_id: int = deserialize("int", method_params[1])
                ans = serialize(obj.get(index, snap_id))
                output.append(ans)

    print("\noutput:", join_array(output))
