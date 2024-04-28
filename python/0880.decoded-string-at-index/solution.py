# Created by Jones at 2024/04/28 21:35
# leetgo: 1.4.5
# https://leetcode.cn/problems/decoded-string-at-index/

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
    def decodeAtIndex(self, s: str, k: int) -> str:
        def dfs(s: str, k: int):
            size = 0
            for i, x in enumerate(s):
                if s[i].isalpha():
                    size += 1
                    if size >= k:
                        return s[i]
                else:
                    x = int(x)
                    if size * x >= k:
                        _k = k % size
                        if _k == 0:
                            _k = size
                        return dfs(s[:i], _k)
                    size *= x

        return dfs(s, k)


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().decodeAtIndex(s, k)
    print("\noutput:", serialize(ans, "string"))
