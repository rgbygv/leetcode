# Created by Jones at 2024/04/12 13:02
# leetgo: 1.4.5
# https://leetcode.com/problems/trapping-rain-water/

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
    def trap(self, height: List[int]) -> int:
        res = 0
        st = [(-1, inf)]

        for i, x in enumerate(height):
            while len(st) > 1 and x > st[-1][1]:
                _, y = st.pop()
                if len(st) > 1:
                    res += (min(x, st[-1][1]) - y) * (i - st[-1][0] - 1)
            # print(i, x, st, res)
            st.append((i, x))
        return res


# @lc code=end

if __name__ == "__main__":
    height: List[int] = deserialize("List[int]", read_line())
    ans = Solution().trap(height)
    print("\noutput:", serialize(ans, "integer"))
