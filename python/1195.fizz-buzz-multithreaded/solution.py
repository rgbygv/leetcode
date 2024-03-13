# Created by Jones at 2024/03/13 20:46
# leetgo: 1.4.2
# https://leetcode.cn/problems/fizz-buzz-multithreaded/

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


class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.lock = Condition()
        self.x = 1

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: "Callable[[], None]") -> None:
        while True:
            with self.lock:
                while self.x <= self.n and not (self.x % 3 == 0 and self.x % 5 != 0):
                    self.lock.wait()
                if self.x > self.n:
                    break
                printFizz()
                self.x += 1
                self.lock.notify_all()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: "Callable[[], None]") -> None:
        while True:
            with self.lock:
                while self.x <= self.n and not (self.x % 3 != 0 and self.x % 5 == 0):
                    self.lock.wait()
                if self.x > self.n:
                    break
                printBuzz()
                self.x += 1
                self.lock.notify_all()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: "Callable[[], None]") -> None:
        while True:
            with self.lock:
                while self.x <= self.n and self.x % 15 != 0:
                    self.lock.wait()
                if self.x > self.n:
                    break
                printFizzBuzz()
                self.x += 1
                self.lock.notify_all()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: "Callable[[int], None]") -> None:
        while True:
            with self.lock:
                while self.x <= self.n and (self.x % 3 == 0 or self.x % 5 == 0):
                    self.lock.wait()
                if self.x > self.n:
                    break
                printNumber(self.x)
                self.x += 1
                self.lock.notify_all()


# @lc code=end

# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().foobar(n)
    print("\noutput:", serialize(ans, "integer"))
