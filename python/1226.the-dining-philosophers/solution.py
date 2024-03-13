# Created by Jones at 2024/03/13 21:07
# leetgo: 1.4.2
# https://leetcode.cn/problems/the-dining-philosophers/

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
from threading import Condition, Lock, Semaphore


class DiningPhilosophers:
    def __init__(self) -> None:
        # self.lock = Condition()
        self.sem = Semaphore(3)
        self.forks = [Lock() for _ in range(5)]

    # call the functions directly to execute, for example, eat()
    def wantsToEat(
        self,
        philosopher: int,
        pickLeftFork: "Callable[[], None]",
        pickRightFork: "Callable[[], None]",
        eat: "Callable[[], None]",
        putLeftFork: "Callable[[], None]",
        putRightFork: "Callable[[], None]",
    ) -> None:
        left = philosopher
        right = (philosopher + 1) % 5

        self.sem.acquire()
        self.forks[left].acquire()
        self.forks[right].acquire()

        pickLeftFork()
        pickRightFork()
        eat()
        putRightFork()
        putLeftFork()

        self.forks[left].release()
        self.forks[right].release()
        self.sem.release()


# @lc code=end

# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    target: int = deserialize("int", read_line())
    ans = Solution().foobar(target)
    print("\noutput:", serialize(ans, "integer"))
