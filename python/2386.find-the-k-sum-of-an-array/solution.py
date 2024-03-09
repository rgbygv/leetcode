# Created by Jones at 2024/03/09 13:09
# leetgo: 1.4.1
# https://leetcode.cn/problems/find-the-k-sum-of-an-array/

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
    def kSum(self, nums: List[int], k: int) -> int:
        n = len(nums)

        nums.sort()

        i = bisect_left(nums, 0)
        j = i
        while i < n and nums[i] == 0:
            i += 1

        # (0..j) < 0,  (j..i) == 0, (i..n) > 0
        mx = sum(nums[i:])
        cnt = i - j
        # 0 can be chosen or don't choose and k <= min(2000,2**n)
        size = 2 ** min(cnt, 11)
        if size >= k:
            return mx

        # add a neg, or del a pos to change
        # q = [(-mx, j - 1, i)]
        s, left, right = mx, j - 1, i
        print(nums)
        while k > 0:
            # s, left, right = heappop(q)
            # s = -s
            print(k, s, left, right)
            if s < 0:
                k -= 1  # empty sub array
                if k == 0:
                    return 0
            if k <= size:
                return s
            k -= size
            if left == -1 or -nums[left] >= nums[right]:
                s -= nums[right]
                right += 1
            else:
                s += nums[left]
                left -= 1
        return -1


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().kSum(nums, k)
    print("\noutput:", serialize(ans, "long"))
