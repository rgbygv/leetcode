# Created by Jones at 2024/02/04 11:07
# leetgo: 1.4.1
# https://leetcode.cn/problems/nim-game/

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
    def canWinNim(self, n: int) -> bool:
        if n < 4:
            return True
        return n % 4 != 0

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().canWinNim(n)
    print("\noutput:", serialize(ans, "boolean"))
