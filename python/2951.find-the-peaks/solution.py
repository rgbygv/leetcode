# Created by Jones at 2024/05/28 10:44
# leetgo: 1.4.7
# https://leetcode.cn/problems/find-the-peaks/

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
    def findPeaks(self, mountain: List[int]) -> List[int]:
        res = []
        for i in range(1, len(mountain) - 1):
            if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]:
                res.append(i)
        return res


# @lc code=end

if __name__ == "__main__":
    mountain: List[int] = deserialize("List[int]", read_line())
    ans = Solution().findPeaks(mountain)
    print("\noutput:", serialize(ans, "integer[]"))
