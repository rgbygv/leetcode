# Created by Jones at 2023/12/21 13:26
# leetgo: dev
# https://leetcode.cn/problems/beautiful-towers-ii/

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
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        n = len(maxHeights)
        right = [0] * n
        st = [n]
        s = 0

        for i in range(n - 1, -1, -1):
            x = maxHeights[i]
            while len(st) > 1 and x < maxHeights[st[-1]]:
                last = st.pop()
                s += (x - maxHeights[last]) * (st[-1] - last)
            s += x
            st.append(i)
            right[i] = s

        s = 0
        st = [-1]
        # print(right)
        res = 0
        for i in range(n):
            x = maxHeights[i]
            while len(st) > 1 and x < maxHeights[st[-1]]:
                last = st.pop()
                s += (x - maxHeights[last]) * (last - st[-1])
            res = max(res, s + right[i])
            s += x
            st.append(i)
        return res


# @lc code=end

if __name__ == "__main__":
    maxHeights: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maximumSumOfHeights(maxHeights)

    print("\noutput:", serialize(ans))
