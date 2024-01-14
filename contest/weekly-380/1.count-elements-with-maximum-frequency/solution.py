# Created by Jones at 2024/01/14 10:30
# leetgo: dev
# https://leetcode.cn/problems/count-elements-with-maximum-frequency/
# https://leetcode.cn/contest/weekly-contest-380/problems/count-elements-with-maximum-frequency/

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


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        x = max(cnt.values())
        return sum(v for i, v in cnt.items() if v == x)


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxFrequencyElements(nums)

    print("\noutput:", serialize(ans))
