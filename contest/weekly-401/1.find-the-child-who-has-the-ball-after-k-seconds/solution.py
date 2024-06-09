# Created by Jones at 2024/06/09 20:59
# leetgo: 1.4.7
# https://leetcode.cn/problems/find-the-child-who-has-the-ball-after-k-seconds/
# https://leetcode.cn/contest/weekly-contest-401/problems/find-the-child-who-has-the-ball-after-k-seconds/

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
    def numberOfChild(self, n: int, k: int) -> int:
        a, b = divmod(k, 2 * (n - 1))
        if b <= n - 1:
            return b
        return n - 1 - (b - (n - 1))


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().numberOfChild(n, k)
    print("\noutput:", serialize(ans, "integer"))
