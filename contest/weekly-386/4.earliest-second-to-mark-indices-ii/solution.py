# Created by Jones at 2024/02/25 19:31
# leetgo: 1.4.1
# https://leetcode.cn/problems/earliest-second-to-mark-indices-ii/
# https://leetcode.cn/contest/weekly-contest-386/problems/earliest-second-to-mark-indices-ii/

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
    def earliestSecondToMarkIndices(self, nums: List[int], change: List[int]) -> int:
        n = len(nums)
        m = len(change)
        if n > m:
            return -1
        change = [x - 1 for x in change]

        l = n
        r = m
        while l <= r:
            mid = (l + r) >> 1

            def check(mid):
                # the last appear point can be marked latest

                # the last operation must be mark
                cnt = 0
                mark = [False] * n
                for i in range(mid - 1, -1, -1):
                    x = change[i]
                    if cnt == 0:
                        cnt += 1
                    else:
                        # try mark this point
                        if not mark[x]:
                            if cnt > 0 or cnt == 0 and nums[x] == 0:
                                mark[x] = True
                                cnt -= int(nums[x] != 0)
                        else:
                            cnt += 1
                return all(x for x in mark)
                #         cnt += 1
                # print(mid, cnt, f)
                # for i, x in enumerate(f):
                #     if not x and nums[i] > 0:
                #         cnt -= nums[i]
                # return cnt >= n

            # print(l, r, check(mid))
            if check(mid):
                r = mid - 1
            else:
                l = mid + 1
        if l == m + 1:
            return -1
        return l


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    changeIndices: List[int] = deserialize("List[int]", read_line())
    ans = Solution().earliestSecondToMarkIndices(nums, changeIndices)
    print("\noutput:", serialize(ans, "integer"))
