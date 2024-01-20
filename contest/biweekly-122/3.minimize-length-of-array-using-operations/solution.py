# Created by Jones at 2024/01/20 22:30
# leetgo: dev
# https://leetcode.cn/problems/minimize-length-of-array-using-operations/
# https://leetcode.cn/contest/biweekly-contest-122/problems/minimize-length-of-array-using-operations/

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
    def minimumArrayLength(self, nums: List[int]) -> int:
        nums.sort()
        cnt = Counter(nums)
        res = (cnt[nums[0]] + 1) // 2
        if nums[0] == 1:
            return res
        # check if can get x < nums[0]
        for x in nums:
            if x % nums[0] != 0:
                return 1
        return res


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minimumArrayLength(nums)

    print("\noutput:", serialize(ans))
