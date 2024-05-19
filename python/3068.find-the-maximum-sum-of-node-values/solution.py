# Created by Jones at 2024/05/19 15:12
# leetgo: 1.4.7
# https://leetcode.com/problems/find-the-maximum-sum-of-node-values/

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
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        """
        - `2 <= n == nums.length <= 2 * 10⁴`
        - `1 <= k <= 10⁹`
        - `0 <= nums[i] <= 10⁹`
        - `edges.length == n - 1`
        - `edges[i].length == 2`
        - `0 <= edges[i][0], edges[i][1] <= n - 1`
        - The input is generated such that `edges` represent a valid tree.
        """
        # n = len(nums)
        # g = [[] for _ in range(n)]

        # for x, y in edges:
        #     g[x].append(y)
        #     g[y].append(x)

        # if the tree is all connected

        pos = inf
        cnt = 0
        res = 0
        for x in nums:
            if (y := k ^ x) > x:
                res += y
                cnt ^= 1
                if (d := y - x) < pos:
                    pos = d
            else:
                res += x
                if (d := x - y) < pos:
                    pos = d
        if cnt == 0:
            return res
        return res - pos


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().maximumValueSum(nums, k, edges)
    print("\noutput:", serialize(ans, "long"))
