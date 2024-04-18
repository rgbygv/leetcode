# Created by Jones at 2024/04/18 09:59
# leetgo: 1.4.5
# https://leetcode.cn/problems/find-original-array-from-doubled-array/

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
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        if n & 1:
            return []
        m = n >> 1
        changed.sort()
        # double end
        res = []
        i = j = n - 1
        vis = [False] * n
        while i >= 0:
            while vis[j]:
                j -= 1
            i = min(i, j - 1)
            while i >= 0 and changed[i] * 2 != changed[j]:
                i -= 1
            if i < 0:
                break
            res.append(changed[i])
            vis[i] = True
            i -= 1
            j -= 1
        # print(i, j, changed)
        if len(res) == m:
            return res
        return []

        # here is situation of rolate

        # i = 0
        # while i < m and changed[(i + m) % n] == 2 * changed[i]:
        #     i += 1
        # if i == m:
        #     return changed[:m]

        # # now a[..i] is good, check a[(n-(m-i))..n]
        # # print(n, i ,m)
        # for j in range(n - (m - i), n):
        #     if changed[(j + m) % n] != 2 * changed[j]:
        #         return []

        # return changed[n - (m - i) : n] + changed[:i]


# @lc code=end

if __name__ == "__main__":
    changed: List[int] = deserialize("List[int]", read_line())
    ans = Solution().findOriginalArray(changed)
    print("\noutput:", serialize(ans, "integer[]"))
