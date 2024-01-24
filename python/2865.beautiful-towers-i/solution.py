# Created by Jones at 2024/01/24 19:42
# leetgo: dev
# https://leetcode.cn/problems/beautiful-towers-i/

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
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        n = len(maxHeights)

        def f(maxHeights):
            left = [0] * (n + 1)
            st = []
            for i, x in enumerate(maxHeights):
                while st and x <= maxHeights[st[-1]]:
                    st.pop()
                j = st[-1] if st else -1
                left[i] = (i - j) * x + left[j]
                st.append(i)
            return left

        left = f(maxHeights)
        right = f(maxHeights[::-1])[::-1]
        # print(left, right)

        return max(left[i] + right[i + 1] - x for i, x in enumerate(maxHeights))


# @lc code=end

if __name__ == "__main__":
    maxHeights: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maximumSumOfHeights(maxHeights)

    print("\noutput:", serialize(ans))
