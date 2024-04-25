# Created by Jones at 2024/04/25 14:10
# leetgo: 1.4.5
# https://leetcode.com/problems/longest-ideal-subsequence/

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
    def longestIdealString(self, s: str, k: int) -> int:
        last = [0] * 26

        for ch in s:
            x = ord(ch) - ord("a")
            begin = max(0, x - k)
            end = min(25, x + k)

            res = max(last[d] + 1 for d in range(begin, end + 1))
            last[x] = res

        return max(last)


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().longestIdealString(s, k)
    print("\noutput:", serialize(ans, "integer"))
