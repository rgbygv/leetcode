# Created by Jones at 2024/03/06 20:23
# leetgo: 1.4.1
# https://leetcode.cn/problems/find-the-k-or-of-an-array/

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
    def findKOr(self, nums: List[int], k: int) -> int:
        N = 31
        cnt = [0] * N
        for x in nums:
            for i in range(N):
                if x >> i & 1:
                    cnt[i] += 1
        return sum(1 << i for i, x in enumerate(cnt) if x >= k)


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().findKOr(nums, k)
    print("\noutput:", serialize(ans, "integer"))
