# Created by Jones at 2023/12/23 18:36
# leetgo: dev
# https://leetcode.cn/problems/remove-stones-to-minimize-the-total/

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
from string import ascii_lowercase
from typing import List, Optional

# @lc code=begin
# from sortedcontainers import SortedList


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        q = [-x for x in piles]
        heapify(q)

        for _ in range(k):
            x = -heappop(q)
            x = (x + 1) // 2
            heappush(q, -x)

        return -sum(q)


# @lc code=end

if __name__ == "__main__":
    piles: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().minStoneSum(piles, k)

    print("\noutput:", serialize(ans))
