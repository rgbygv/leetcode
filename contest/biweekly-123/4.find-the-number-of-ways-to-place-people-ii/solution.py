# Created by Jones at 2024/02/06 16:09
# leetgo: 1.4.1
# https://leetcode.cn/problems/find-the-number-of-ways-to-place-people-ii/
# https://leetcode.cn/contest/biweekly-contest-123/problems/find-the-number-of-ways-to-place-people-ii/

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
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda e:(e[0], -e[1]))
        n = len(points)
        res = 0
        for i in range(n):
            x1,y1 = points[i]
            q = SortedList()
            q.add(y1)
            for j in range(i+1,n):
                x2,y2 = points[j]
                if y1 >= y2:
                    l = q.bisect_left(y2)
                    r = q.bisect_right(y1) - 1
                    res += l == r
                q.add(y2)
        return res

# @lc code=end

if __name__ == "__main__":
    points: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().numberOfPairs(points)
    print("\noutput:", serialize(ans, "integer"))
