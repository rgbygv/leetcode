# Created by Jones at 2023/11/27 13:36
# leetgo: dev
# https://leetcode.cn/problems/sum-of-subarray-minimums/

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
    def sumSubarrayMins(self, a: List[int]) -> int:
        n = len(a)
        left = [0] * n
        right = [n - 1] * n
        st = []
        for i, x in enumerate(a):
            while st and x <= a[st[-1]]:
                right[st.pop()] = i - 1
            if st:
                left[i] = st[-1] + 1
            st.append(i)
        # print(left, right)
        mod = 10**9 + 7
        res = 0
        for i in range(n):
            res += a[i] * (right[i] - i + 1) * (i - left[i] + 1)
            res %= mod
        return res


# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    ans = Solution().sumSubarrayMins(arr)

    print("\noutput:", serialize(ans))
