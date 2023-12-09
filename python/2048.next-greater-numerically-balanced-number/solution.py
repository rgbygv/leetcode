# Created by Jones at 2023/12/09 13:51
# leetgo: dev
# https://leetcode.cn/problems/next-greater-numerically-balanced-number/

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
    def nextBeautifulNumber(self, num: int) -> int:
        # 1e6
        # 1224444
        for x in range(num + 1, int(1e6)):
            cnt = [0] * 10
            y = x
            while y:
                cnt[y % 10] += 1
                y //= 10

            def check(cnt):
                for i, x in enumerate(cnt):
                    if x > 0 and i != x:
                        return False
                return True

            if check(cnt):
                return x
        return 1224444


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().nextBeautifulNumber(n)

    print("\noutput:", serialize(ans))
