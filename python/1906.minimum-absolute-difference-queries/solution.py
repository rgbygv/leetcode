# Created by Jones at 2024/05/30 14:20
# leetgo: 1.4.7
# https://leetcode.cn/problems/minimum-absolute-difference-queries/

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
    def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        """
        - `2 <= nums.length <= 10⁵`
        - `1 <= nums[i] <= 100`
        - `1 <= queries.length <= 2 * 10⁴`
        - `0 <= lᵢ < rᵢ < nums.length`
        """
        N = max(nums) + 1
        g = [[] for _ in range(N)]
        res = []
        for i, x in enumerate(nums):
            g[x].append(i)

        for l, r in queries:
            # check if x in [l, r]
            pre = None
            ans = inf
            for x in range(1, N):
                v = g[x]
                i = bisect_left(v, l)
                if i < len(v) and v[i] <= r:
                    if pre is None:
                        pre = x
                    else:
                        ans = min(ans, x - pre)
                        pre = x
            if ans == inf:
                res.append(-1)
            else:
                res.append(ans)
        return res


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    queries: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().minDifference(nums, queries)
    print("\noutput:", serialize(ans, "integer[]"))
