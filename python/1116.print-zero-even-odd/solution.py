# Created by Jones at 2024/03/13 20:10
# leetgo: 1.4.2
# https://leetcode.cn/problems/print-zero-even-odd/

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


class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.lock = Condition()
        self.zero_turn = True
        self.num = 0

    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: "Callable[[int], None]") -> None:
        for _ in range(self.n):
            with self.lock:
                while not self.zero_turn:
                    self.lock.wait()
                self.zero_turn = False
                printNumber(0)
                self.num += 1
                self.lock.notify_all()

    def even(self, printNumber: "Callable[[int], None]") -> None:
        for _ in range(self.n // 2):
            with self.lock:
                while self.zero_turn or self.num & 1 == 1:
                    self.lock.wait()
                self.zero_turn = True
                printNumber(self.num)
                self.lock.notify_all()

    def odd(self, printNumber: "Callable[[int], None]") -> None:
        for _ in range((self.n + 1) // 2):
            with self.lock:
                while self.zero_turn or self.num & 1 == 0:
                    self.lock.wait()
                self.zero_turn = True
                printNumber(self.num)
                self.lock.notify_all()


# @lc code=end

# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().printZeroEvenOdd(n)
    print("\noutput:", serialize(ans, "integer"))
