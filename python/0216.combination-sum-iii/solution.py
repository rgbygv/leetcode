# Created by Jones at 2024/04/21 13:04
# leetgo: 1.4.5
# https://leetcode.cn/problems/combination-sum-iii/

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
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # - `2 <= k <= 9`
        # - `1 <= n <= 60`

        res = []
        path = []

        def dfs(i: int, k: int, n: int):
            """
            use number `i`, have `k` times, the rest of `n`

            `O(i * k * n)`
            """
            if k < 0 or n < 0:
                return
            if i >= 10:  # only use number 1 <= x <= 9
                if k == 0 and n == 0:
                    res.append(path[:])
                return
            # use i
            if i <= n:
                path.append(i)
                dfs(i + 1, k - 1, n - i)
                path.pop()
            # don't use i
            dfs(i + 1, k, n)

        dfs(1, k, n)
        return res


# @lc code=end

if __name__ == "__main__":
    k: int = deserialize("int", read_line())
    n: int = deserialize("int", read_line())
    ans = Solution().combinationSum3(k, n)
    print("\noutput:", serialize(ans, "integer[][]"))
