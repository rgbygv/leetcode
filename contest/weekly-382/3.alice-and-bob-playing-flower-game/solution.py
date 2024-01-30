# Created by Jones at 2024/01/30 21:01
# leetgo: dev
# https://leetcode.cn/problems/alice-and-bob-playing-flower-game/
# https://leetcode.cn/contest/weekly-contest-382/problems/alice-and-bob-playing-flower-game/

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
    def flowerGame(self, n: int, m: int) -> int:
        # (x + y) & 1 == 0
        if n > m:
            n, m = m, n
        res = 0
        for x in range(1, n+1):
            if x & 1:
                res += m // 2
            else:
                res += (m+1) // 2
        return res
            

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    m: int = deserialize("int", read_line())
    ans = Solution().flowerGame(n, m)
    print("\noutput:", serialize(ans, "long"))
