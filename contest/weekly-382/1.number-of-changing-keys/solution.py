# Created by Jones at 2024/01/30 21:01
# leetgo: dev
# https://leetcode.cn/problems/number-of-changing-keys/
# https://leetcode.cn/contest/weekly-contest-382/problems/number-of-changing-keys/

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
    def countKeyChanges(self, s: str) -> int:
        return sum(x != y for x,y in pairwise(s.lower()))

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().countKeyChanges(s)
    print("\noutput:", serialize(ans, "integer"))
