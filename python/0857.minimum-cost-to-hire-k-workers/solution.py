# Created by Jones at 2024/05/02 14:33
# leetgo: 1.4.5
# https://leetcode.cn/problems/minimum-cost-to-hire-k-workers/

from typing import *
from leetgo_py import *

from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from functools import cache, cmp_to_key, lru_cache, reduce
from heapq import heapify, heappop, heappush, heappushpop, heapreplace
from icecream import ic
from itertools import accumulate, chain, count, pairwise, zip_longest
from math import ceil, comb, floor, gcd, inf, isqrt, lcm, log2, perm, sqrt
from operator import xor
from pprint import pprint
from string import ascii_lowercase
from typing import List, Optional


# @lc code=begin
class worker:
    def __init__(self, q: int, w: int) -> None:
        self.q = q
        self.w = w

    def __lt__(self, other: "worker") -> bool:
        return self.w * other.q < other.w * self.q


class Solution:
    def mincostToHireWorkers(
        self, quality: List[int], wage: List[int], k: int
    ) -> float:
        # we should find the best worker w/q
        n = len(quality)
        # best_workers = sorted(range(n), key=lambda i: worker(quality[i], wage[i]))
        best_workers = sorted(range(n), key=lambda i: wage[i] / quality[i])
        # print(best_workers)
        # we should use the rate of worst people in the q
        # use rate of worst people is valid for all workers i < j
        res = inf
        s = 0
        q = []
        for idx in range(k - 1):
            cur = quality[best_workers[idx]]
            heappush(q, -cur)
            s += cur
        for idx in range(k - 1, n):
            i = best_workers[idx]
            cur = quality[i]
            heappush(q, -cur)
            s += cur
            res = min(res, s / cur * wage[i])
            s += heappop(q)

        return res



# @lc code=end

if __name__ == "__main__":
    quality: List[int] = deserialize("List[int]", read_line())
    wage: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().mincostToHireWorkers(quality, wage, k)
    print("\noutput:", serialize(ans, "double"))
