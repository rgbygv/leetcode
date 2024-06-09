# Created by Jones at 2024/06/09 20:59
# leetgo: 1.4.7
# https://leetcode.cn/problems/find-the-n-th-value-after-k-seconds/
# https://leetcode.cn/contest/weekly-contest-401/problems/find-the-n-th-value-after-k-seconds/

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
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        mod = 10**9 + 7
        f = [1] * n
        for _ in range(k):
            for j in range(1, n):
                f[j] += f[j - 1]
                f[j] %= mod
        return f[-1]


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().valueAfterKSeconds(n, k)
    print("\noutput:", serialize(ans, "integer"))
