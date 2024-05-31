# Created by Jones at 2024/05/31 08:57
# leetgo: 1.4.7
# https://leetcode.cn/problems/find-missing-and-repeated-values/

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
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid) ** 2
        cnt = Counter()
        s = 0
        res = []
        for row in grid:
            for x in row:
                cnt[x] += 1
                s += x
                if cnt[x] == 2:
                    res.append(x)

        res.append((1 + n) * n // 2 + res[0] - s)
        return res


# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().findMissingAndRepeatedValues(grid)
    print("\noutput:", serialize(ans, "integer[]"))
