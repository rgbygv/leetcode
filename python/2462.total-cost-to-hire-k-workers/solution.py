# Created by Jones at 2024/05/01 13:05
# leetgo: 1.4.5
# https://leetcode.cn/problems/total-cost-to-hire-k-workers/

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


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        if candidates * 2 >= n:
            return sum(sorted(costs)[:k])

        # use heap to simulate the process
        q = []
        for i in range(candidates):
            heappush(q, (costs[i], 0))

        for i in range(n - 1, n - 1 - candidates, -1):
            heappush(q, (costs[i], 1))

        left_idx = candidates - 1
        right_idx = n - candidates

        res = 0
        for _ in range(k):
            # print(q)
            c, flg = heappop(q)
            res += c
            if left_idx + 1 < right_idx:
                if flg == 0:  # left half
                    left_idx += 1
                    heappush(q, (costs[left_idx], flg))
                else:
                    right_idx -= 1
                    heappush(q, (costs[right_idx], flg))
        return res


# @lc code=end

if __name__ == "__main__":
    costs: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    candidates: int = deserialize("int", read_line())
    ans = Solution().totalCost(costs, k, candidates)
    print("\noutput:", serialize(ans, "long"))
