# Created by Jones at 2024/06/09 14:36
# leetgo: 1.4.7
# https://leetcode.com/problems/subarray-sums-divisible-by-k/

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
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        cnt = Counter()
        cnt[0] += 1
        s = 0
        res = 0
        for x in nums:
            s = (s + x) % k
            res += cnt[s]
            cnt[s] += 1
        return res


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().subarraysDivByK(nums, k)
    print("\noutput:", serialize(ans, "integer"))
