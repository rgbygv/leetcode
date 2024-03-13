# Created by Jones at 2024/03/13 20:32
# leetgo: 1.4.2
# https://leetcode.cn/problems/building-h2o/

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
from threading import Condition


class H2O:
    def __init__(self):
        self.lock = Condition()
        self.h = 2
        self.o = 1

    def start(self):
        self.h = 2
        self.o = 1

    def hydrogen(self, releaseHydrogen: "Callable[[], None]") -> None:
        with self.lock:
            while self.h == 0:
                self.lock.wait()
            self.h -= 1
            if self.h == 0 and self.o == 0:
                self.start()
            releaseHydrogen()
            self.lock.notify_all()

    def oxygen(self, releaseOxygen: "Callable[[], None]") -> None:
        with self.lock:
            while self.o == 0:
                self.lock.wait()
            self.o -= 1
            if self.h == 0:
                self.start()
            releaseOxygen()
            self.lock.notify_all()


# @lc code=end

# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    water: str = deserialize("str", read_line())
    ans = Solution().H2O(water)
    print("\noutput:", serialize(ans, "string"))
