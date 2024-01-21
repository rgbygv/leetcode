# Created by Jones at 2024/01/21 15:10
# leetgo: dev
# https://leetcode.cn/problems/count-the-number-of-houses-at-a-certain-distance-ii/
# https://leetcode.cn/contest/weekly-contest-381/problems/count-the-number-of-houses-at-a-certain-distance-ii/

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
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        if x == y:
            res = list(range(n - 1, -1, -1))
            return [2 * x for x in res] + [0] * (n - len(res))
        x, y = sorted((x, y))

        diff = [0] * (n + 1)

        mid = ceil((x + y + 1) / 2)
        # 0 ... x ... i ... y ... n
        for left in range(x):
            """
            for i in range(y,n+1):
                f[i - left] -= 1
                f[x - left + 1 + i - y] += 1

            for i in range(mid, y):
                f[i - left] -= 1
                f[x - left + 1 + y - i] += 1


            """
        # 0 ... x ... mid ... y ... n
        for left in range(x, mid):
            """
            for i in range(y, n+1):
                f[n - left] -= 1
                f[left - x + 1 + i - y ] += 1
            """


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    x: int = deserialize("int", read_line())
    y: int = deserialize("int", read_line())
    ans = Solution().countOfPairs(n, x, y)

    print("\noutput:", serialize(ans))
