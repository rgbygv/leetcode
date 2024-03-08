# Created by Jones at 2024/03/08 20:09
# leetgo: 1.4.1
# https://leetcode.cn/problems/find-the-minimum-possible-sum-of-a-beautiful-array/

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
    def minimumPossibleSum(self, n: int, target: int) -> int:
        mod = 10**9 + 7

        """
        1..=target/2
        target..
        """
        mid = target // 2
        if n <= mid:
            return (1 + n) * n // 2 % mod
        rest = n - mid
        return ((1 + mid) * mid // 2 + (target + target - 1 + rest) * rest // 2) % mod


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().minimumPossibleSum(n, target)
    print("\noutput:", serialize(ans, "integer"))
