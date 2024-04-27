# Created by Jones at 2024/04/27 19:30
# leetgo: 1.4.5
# https://leetcode.cn/problems/soup-servings/

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


@cache
def dfs(a: int, b: int):
    if a <= 0:
        if b <= 0:
            #  a empty same as b
            return 0.5
        # a empty first
        return 1
    if b <= 0:
        # b empth first
        return 0
    return 0.25 * (
        dfs(a - 100, b)
        + dfs(a - 75, b - 25)
        + dfs(a - 50, b - 50)
        + dfs(a - 25, b - 75)
    )


limit = 10000
while dfs(limit, limit) < 1:
    limit += 10000


class Solution:
    def soupServings(self, n: int) -> float:
        # 1. Serve `100` ml of **soup A** and `0` ml of **soup B**,
        # 2. Serve `75` ml of **soup A** and `25` ml of **soup B**,
        # 3. Serve `50` ml of **soup A** and `50` ml of **soup B**, and
        # 4. Serve `25` ml of **soup A** and `75` ml of **soup B**.
        # - `0 <= n <= 10⁹`

        # we can assume when n is bigger enough, a is must be empty first
        if n > limit:
            return 1
        return dfs(n, n)


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().soupServings(n)
    print("\noutput:", serialize(ans, "double"))
