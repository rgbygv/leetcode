# Created by Jones at 2024/05/05 15:50
# leetgo: 1.4.6
# https://leetcode.cn/problems/stone-game-ii/

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
    def stoneGameII(self, piles: List[int]) -> int:
        # - `1 <= piles.length <= 100`
        # - `1 <= piles[i] <= 10⁴`
        n = len(piles)

        p = list(accumulate(piles, initial=0))

        @cache
        def dfs(i: int, m: int, ok: bool):
            if (n - i) <= 2 * m:
                return (p[-1] - p[i]) if ok else 0
            if ok:  # max
                res = -inf
                for cur in range(1, 2 * m + 1):
                    res = max(
                        res,
                        p[i + cur] - p[i] + dfs(i + cur, max(m, cur), 1 - ok),
                    )
                return res
            else:  # min
                res = inf
                for cur in range(1, 2 * m + 1):
                    res = min(
                        res,
                        dfs(i + cur, max(m, cur), 1 - ok),
                    )
                return res

        return dfs(0, 1, 1)


# @lc code=end

if __name__ == "__main__":
    piles: List[int] = deserialize("List[int]", read_line())
    ans = Solution().stoneGameII(piles)
    print("\noutput:", serialize(ans, "integer"))
