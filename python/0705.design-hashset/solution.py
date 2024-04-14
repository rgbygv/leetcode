# Created by Jones at 2024/04/14 12:51
# leetgo: 1.4.5
# https://leetcode.cn/problems/design-hashset/

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

N = int(1e6) + 1


class MyHashSet:
    def __init__(self):
        # We can use a small bucket and use (key % N) as key
        # and each bucket we can use a linkedlist
        self.bucket = [False] * N

    def add(self, key: int) -> None:
        self.bucket[key] = True

    def remove(self, key: int) -> None:
        self.bucket[key] = False

    def contains(self, key: int) -> bool:
        return self.bucket[key]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    obj = MyHashSet()

    for i in range(1, len(ops)):
        match ops[i]:
            case "add":
                method_params = split_array(params[i])
                key: int = deserialize("int", method_params[0])
                obj.add(key)
                output.append("null")
            case "remove":
                method_params = split_array(params[i])
                key: int = deserialize("int", method_params[0])
                obj.remove(key)
                output.append("null")
            case "contains":
                method_params = split_array(params[i])
                key: int = deserialize("int", method_params[0])
                ans = serialize(obj.contains(key))
                output.append(ans)

    print("\noutput:", join_array(output))
