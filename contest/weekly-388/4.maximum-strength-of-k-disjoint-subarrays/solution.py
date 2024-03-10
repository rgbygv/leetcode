# Created by Jones at 2024/03/10 13:54
# leetgo: 1.4.1
# https://leetcode.cn/problems/maximum-strength-of-k-disjoint-subarrays/
# https://leetcode.cn/contest/weekly-contest-388/problems/maximum-strength-of-k-disjoint-subarrays/

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
    def maximumStrength(self, nums: List[int], k: int) -> int:
        n = len(nums)

        f = [[-inf] * (k + 1) for _ in range(n + 1)]

        f[0][0] = 0

        """
        
        """
        for i, x in enumerate(nums, 1):
            for j in range(1, k + 1):
                d = sum(nums[z : i + 1]) * (k + 1 - j)
                f[i][j] = f[z][j - 1]


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().maximumStrength(nums, k)
    print("\noutput:", serialize(ans, "long"))
