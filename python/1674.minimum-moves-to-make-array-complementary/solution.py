# Created by Jones at 2024/05/10 15:56
# leetgo: 1.4.7
# https://leetcode.cn/problems/minimum-moves-to-make-array-complementary/

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
from sortedcontainers import SortedList


class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        """
        - `n == nums.length`
        - `2 <= n <= 10⁵`
        - `1 <= nums[i] <= limit <= 10⁵`
        - `n` is even.
        """

        # if we know the sum
        # if x + y == sum => 0
        # if x + y != sum => at least 1, at most 2

        # consider 0 .. i, if max(x,y) + limit < target: need 2
        # consider j .. n, if min(x,y) + 1 > target: need 2
        n = len(nums)
        diff = [0] * (2 * limit + 2)
        i, j = 0, n - 1
        while i < j:
            x, y = sorted((nums[i], nums[j]))
            # [2, 2 * limit] + 2
            diff[2] += 2
            diff[2 * limit + 1] -= 2

            # [1+x, y+limit] + 1
            diff[x + 1] += -1
            diff[y + limit + 1] -= -1

            # [x + y] + 0
            diff[x + y] += -1
            diff[x + y + 1] -= -1

            i += 1
            j -= 1

        res = inf
        d = 0
        for i in range(2, len(diff) - 1):
            d += diff[i]
            if d < res:
                res = d
        return res

        # this is wrong version, because sum maybe not in q

        # the sum should in q
        # res = inf
        # n = len(q)
        # i = 0
        # pre = SortedList()
        # suf = SortedList(mn for _, mn, _ in q)

        # while i < n:
        #     j = i
        #     while j < n and q[j][0] == q[i][0]:
        #         suf.remove(q[j][1])
        #         j += 1
        #     target, *_ = q[i]
        #     cur = i + n - j
        #     # 0..i..j..n
        #     # consider 0 .. i, if max(x,y) + limit < target: need 2
        #     cur += pre.bisect_left(target - limit)
        #     # consider j .. n, if min(x,y) + 1 > target: need 2
        #     cur += len(suf) - suf.bisect_right(target - 1)
        #     ic(q, pre, suf, cur, target - limit, target - 1)
        #     res = min(res, cur)
        #     for k in range(i, j):
        #         pre.add(q[k][2])
        #     i = j

        # return res


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    limit: int = deserialize("int", read_line())
    ans = Solution().minMoves(nums, limit)
    print("\noutput:", serialize(ans, "integer"))
