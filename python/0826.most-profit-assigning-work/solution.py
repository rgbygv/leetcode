# Created by Jones at 2024/05/17 12:32
# leetgo: 1.4.7
# https://leetcode.cn/problems/most-profit-assigning-work/

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


class Solution:
    def maxProfitAssignment(
        self, difficulty: List[int], profit: List[int], worker: List[int]
    ) -> int:
        q = sorted(zip(difficulty, profit))
        st = []
        for d, p in q:
            if st and p <= st[-1][-1]:
                continue
            st.append((d, p))
        res = 0
        for w in worker:
            i = bisect_right(st, w, key=lambda e: e[0]) - 1
            if i >= 0:
                res += st[i][1]
        return res


# @lc code=end

if __name__ == "__main__":
    difficulty: List[int] = deserialize("List[int]", read_line())
    profit: List[int] = deserialize("List[int]", read_line())
    worker: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxProfitAssignment(difficulty, profit, worker)
    print("\noutput:", serialize(ans, "integer"))
