# Created by Jones at 2024/02/25 19:31
# leetgo: 1.4.1
# https://leetcode.cn/problems/earliest-second-to-mark-indices-i/
# https://leetcode.cn/contest/weekly-contest-386/problems/earliest-second-to-mark-indices-i/

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
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    changeIndices: List[int] = deserialize("List[int]", read_line())
    ans = Solution().earliestSecondToMarkIndices(nums, changeIndices)
    print("\noutput:", serialize(ans, "integer"))
