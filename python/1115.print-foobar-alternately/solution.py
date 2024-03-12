# Created by Jones at 2024/03/12 21:37
# leetgo: 1.4.2
# https://leetcode.cn/problems/print-foobar-alternately/

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


class FooBar:
    def __init__(self, n):
        self.n = n
        self.lock = Condition()
        self.cnt = 0

    def foo(self, printFoo: "Callable[[], None]") -> None:
        for i in range(self.n):
            with self.lock:
                while self.cnt != 0:
                    self.lock.wait()
                self.cnt = 1
                printFoo()
                self.lock.notify_all()

    def bar(self, printBar: "Callable[[], None]") -> None:
        for i in range(self.n):
            # printBar() outputs "bar". Do not change or remove this line.
            with self.lock:
                while self.cnt != 1:
                    self.lock.wait()
                self.cnt = 0
                printBar()
                self.lock.notify_all()


# @lc code=end

# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().FooBar(n)
    print("\noutput:", serialize(ans, "integer"))
