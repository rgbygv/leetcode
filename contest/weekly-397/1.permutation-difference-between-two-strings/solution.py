# Created by Jones at 2024/05/12 18:20
# leetgo: 1.4.7
# https://leetcode.cn/problems/permutation-difference-between-two-strings/
# https://leetcode.cn/contest/weekly-contest-397/problems/permutation-difference-between-two-strings/

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
    def findPermutationDifference(self, s: str, t: str) -> int:
        mp = {v: i for i, v in enumerate(t)}
        return sum(abs(i - mp[ch]) for i, ch in enumerate(s))


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    t: str = deserialize("str", read_line())
    ans = Solution().findPermutationDifference(s, t)
    print("\noutput:", serialize(ans, "integer"))
