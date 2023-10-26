# Created by Jones at 2023/10/26 19:27
# leetgo: dev
# https://leetcode.cn/problems/count-the-digits-that-divide-a-number/

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
    def countDigits(self, num: int) -> int:
        x = num
        res = 0
        while x:
            res += num % (x % 10) == 0
            x //= 10
        return res


# @lc code=end

if __name__ == "__main__":
    num: int = deserialize("int", read_line())
    ans = Solution().countDigits(num)

    print("\noutput:", serialize(ans))
