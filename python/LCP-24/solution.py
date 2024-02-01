# Created by Jones at 2024/02/01 12:37
# leetgo: 1.4.1
# https://leetcode.cn/problems/5TxKeK/

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
from sortedcontainers import SortedList


class Solution:
    def numsGame(self, nums: List[int]) -> List[int]:
        # - `1 <= nums.length <= 10^5`
        # - `1 <= nums[i] <= 10^3`

        mod = 10**9 + 7
        nums = [x - i for i, x in enumerate(nums)]
        # now we need make all(x in nums[:i]) is same
        # make all equal to nums[i/2]
        # print(nums)

        n = len(nums)
        f = [0] * n

        left = SortedList()
        right = SortedList()

        sum1 = sum2 = 0

        for i, x in enumerate(nums):
            sum1 += x
            left.add(x)

            if len(left) - len(right) > 1:
                x = left.pop()
                sum1 -= x
                right.add(x)
                sum2 += x
            else:
                if right and left[-1] > right[0]:
                    x = left.pop()
                    sum1 -= x
                    right.add(x)
                    sum2 += x
                    if len(right) > len(left):
                        x = right.pop(0)
                        sum2 -= x
                        sum1 += x
                        left.add(x)

            # print(i, left,sum1,right,sum2)

            n = len(left)
            mid = left[-1]
            f[i] = (n * mid) - sum1 + sum2 - (n - (i&1==0)) * mid
            f[i] %= mod

        return f


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().numsGame(nums)
    print("\noutput:", serialize(ans, "integer[]"))
