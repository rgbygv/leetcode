# Created by Jones at 2024/01/29 13:51
# leetgo: 1.4.1
# https://leetcode.cn/problems/freedom-trail/

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
    def findRotateSteps(self, ring: str, key: str) -> int:
        mp = defaultdict(list)
        for i, ch in enumerate(ring):
            mp[ch].append(i)

        m = len(ring)
        n = len(key)

        @cache
        def dfs(i: int, j: int):
            if i == n:
                return 0
            if ring[j] == key[i]:
                return 1 + dfs(i + 1, j)

            res = inf
            for k in mp[key[i]]:
                if k < j:
                    step = min(j - k, m - j + k)
                else:
                    step = min(k - j, j + m - k)
                res = min(res, 1 + step + dfs(i + 1, k))
            return res

        return dfs(0, 0)


# @lc code=end

if __name__ == "__main__":
    ring: str = deserialize("str", read_line())
    key: str = deserialize("str", read_line())
    ans = Solution().findRotateSteps(ring, key)
    print("\noutput:", serialize(ans))
