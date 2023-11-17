# Created by Jones at 2023/11/17 18:55
# leetgo: dev
# https://leetcode.cn/problems/maximum-sum-queries/

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
    def maximumSumQueries(
        self, nums1: List[int], nums2: List[int], queries: List[List[int]]
    ) -> List[int]:
        q = sorted(zip(nums1, nums2))
        n = len(queries)
        res = [-1] * n
        st = []
        j = len(q) - 1
        for i, (x, y) in sorted(enumerate(queries), key=lambda e: -e[1][0]):
            while j >= 0 and q[j][0] >= x:
                cur_x, cur_y = q[j]
                while st and cur_x + cur_y >= st[-1][1]:
                    st.pop()
                if not st or cur_y > st[-1][0]:
                    st.append((cur_y, cur_x + cur_y))
                j -= 1

            idx = bisect_left(st, y, key=lambda e: e[0])
            if idx < len(st):
                res[i] = st[idx][1]
        return res


# @lc code=end

if __name__ == "__main__":
    nums1: List[int] = deserialize("List[int]", read_line())
    nums2: List[int] = deserialize("List[int]", read_line())
    queries: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().maximumSumQueries(nums1, nums2, queries)

    print("\noutput:", serialize(ans))
