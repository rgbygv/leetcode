# Created by Jones at 2024/02/28 19:06
# leetgo: 1.4.1
# https://leetcode.cn/problems/rectangle-area-ii/

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
from sortedcontainers import SortedList


class Solution:
    def rectangleArea(self, a: List[List[int]]) -> int:
        mod = 10**9 + 7
        res = 0

        h = set()
        q = []
        for i, (x1, y1, x2, y2) in enumerate(a):
            h.add(y1)
            h.add(y2)
            q.append((x1, i, 1))
            q.append((x2, i, -1))
        h = sorted(h)
        m = len(h)
        seg = [0] * (m - 1)

        q.sort()
        n = len(q)
        i = 0
        while i < n:

            def handle(i):
                _, idx, diff = q[i]
                _, y1, _, y2 = a[idx]
                for k in range(m - 1):
                    if y1 <= h[k] and h[k + 1] <= y2:
                        seg[k] += diff

            handle(i)
            j = i + 1
            while j < n and q[j][0] == q[j - 1][0]:
                handle(j)
                j += 1

            if j == n:
                break
            width = q[j][0] - q[j - 1][0]
            for i, cnt in enumerate(seg):
                if cnt > 0:
                    res += width * (h[i + 1] - h[i]) % mod
                    res %= mod
            i = j

        return res


# @lc code=end

if __name__ == "__main__":
    rectangles: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().rectangleArea(rectangles)
    print("\noutput:", serialize(ans, "integer"))
