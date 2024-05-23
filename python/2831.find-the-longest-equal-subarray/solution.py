# Created by Jones at 2024/05/23 16:24
# leetgo: 1.4.7
# https://leetcode.cn/problems/find-the-longest-equal-subarray/

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
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        mp = defaultdict(list)
        # group numbers
        for i, x in enumerate(nums):
            mp[x].append(i)

        res = 0
        for v in mp.values():
            if len(v) < res:
                continue
            l = r = 0
            n = len(v)
            while r < n:
                while r < n and v[r] - v[l] - (r - l) <= k:
                    r += 1
                res = max(res, r - l)
                l += 1
        return res

        # l = 0
        # r = 0
        # res = 0
        # cnt = Counter()
        # mx = 0
        # q = set()
        # while r < n:
        #     while r < n and len(cnt) <= k:
        #         cnt[nums[r]] += 1
        #         if cnt[nums[r]] > mx:
        #             mx = cnt[nums[r]]
        #             q = set([nums[r]])
        #         elif cnt[nums[r]] == mx:
        #             q.add(nums[r])
        #         r += 1
        #     # too slow, we maintain max(cnt.values) by ourself
        #     # we can use heapq or sortedlist
        #     # res = max(res, max(cnt.values()))

        #     if r == n:
        #         break
        #     if cnt[nums[l]] == mx:
        #         q.remove(nums[l])
        #     cnt[nums[l]] -= 1
        #     if cnt[nums[l]] == 0:
        #         del cnt[nums[l]]
        #     l += 1
        # return res


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().longestEqualSubarray(nums, k)
    print("\noutput:", serialize(ans, "integer"))
