# Created by Jones at 2024/02/06 16:09
# leetgo: 1.4.1
# https://leetcode.cn/problems/maximum-good-subarray-sum/
# https://leetcode.cn/contest/biweekly-contest-123/problems/maximum-good-subarray-sum/

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
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        seen = {}

        p = list(accumulate(nums,initial=0))
        res = -inf
        for i, x in enumerate(nums):
            for y in (x-k, x+k):
                if y in seen:
                    j = seen[y]
                    res = max(res, p[i+1]-p[j])
            if x not in seen:
                seen[x] = i
            elif p[seen[x]+1] > p[i+1]:
                seen[x] = i
        if res == -inf:
            return 0
        return res


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().maximumSubarraySum(nums, k)
    print("\noutput:", serialize(ans, "long"))
