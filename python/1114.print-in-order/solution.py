# Created by Jones at 2024/03/12 21:18
# leetgo: 1.4.2
# https://leetcode.cn/problems/print-in-order/

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
from threading import Lock, Event, Condition
import time


class Foo:
    def __init__(self):
        self.lock = Condition()
        self.first_done = False
        self.second_done = False

    def first(self, printFirst: "Callable[[], None]") -> None:
        with self.lock:
            printFirst()
            self.first_done = True
            self.lock.notify_all()

    def second(self, printSecond: "Callable[[], None]") -> None:
        with self.lock:
            while not self.first_done:
                self.lock.wait()
            printSecond()
            self.second_done = True
            self.lock.notify()

    def third(self, printThird: "Callable[[], None]") -> None:
        with self.lock:
            while not self.second_done:
                self.lock.wait()
            printThird()


# @lc code=end

# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().foobar(nums)
    print("\noutput:", serialize(ans, "integer"))
