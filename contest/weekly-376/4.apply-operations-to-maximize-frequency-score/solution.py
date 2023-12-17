# Created by Jones at 2023/12/17 14:14
# leetgo: dev
# https://leetcode.cn/problems/apply-operations-to-maximize-frequency-score/
# https://leetcode.cn/contest/weekly-contest-376/problems/apply-operations-to-maximize-frequency-score/

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
from string import ascii_lowercase
from typing import List, Optional

# @lc code=begin
# from sortedcontainers import SortedList


class Solution:
    def maxFrequencyScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        p = list(accumulate(nums, initial=0))
        mx = max(Counter(nums).values())
        if k == 0:
            return mx

        l = 1
        r = n
        while l <= r:
            mid = (l + r) >> 1

            def check(mid):
                for left in range(n - mid + 1):
                    right = left + mid - 1
                    tmp = [(left + right) >> 1]
                    if mid & 1 == 0:
                        tmp.append(tmp[0] + 1)
                    for m in tmp:
                        cur = (
                            nums[m] * (m - left)
                            - (p[m] - p[left])  # sum(nums[left:m])
                            + (p[right + 1] - p[m + 1])  # sum(nums[m + 1 : right + 1])
                            - nums[m] * (right - m)
                        )
                        if cur <= k:
                            # print(left, right, m, cur)
                            return True
                return False

            if mx >= mid or check(mid):
                l = mid + 1
            else:
                r = mid - 1

        return r


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().maxFrequencyScore(nums, k)

    print("\noutput:", serialize(ans))
