# Created by Jones at 2024/04/15 11:43
# leetgo: 1.4.5
# https://leetcode.cn/problems/design-hashmap/

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

N = 10**6 + 1


class MyHashMap:
    def __init__(self):
        self.bucket = [-1] * N

    def put(self, key: int, value: int) -> None:
        self.bucket[key] = value

    def get(self, key: int) -> int:
        return self.bucket[key]

    def remove(self, key: int) -> None:
        self.bucket[key] = -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    obj = MyHashMap()

    for i in range(1, len(ops)):
        match ops[i]:
            case "put":
                method_params = split_array(params[i])
                key: int = deserialize("int", method_params[0])
                value: int = deserialize("int", method_params[1])
                obj.put(key, value)
                output.append("null")
            case "get":
                method_params = split_array(params[i])
                key: int = deserialize("int", method_params[0])
                ans = serialize(obj.get(key))
                output.append(ans)
            case "remove":
                method_params = split_array(params[i])
                key: int = deserialize("int", method_params[0])
                obj.remove(key)
                output.append("null")

    print("\noutput:", join_array(output))
