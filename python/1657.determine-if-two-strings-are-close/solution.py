# Created by Jones at 2023/11/30 12:14
# leetgo: dev
# https://leetcode.cn/problems/determine-if-two-strings-are-close/

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
    def closeStrings(self, word1: str, word2: str) -> bool:
        # op1: order don't matter

        if set(word1) != set(word2):
            return False

        def f(s):
            return sorted(Counter(s).values())

        return f(word1) == f(word2)


# @lc code=end

if __name__ == "__main__":
    word1: str = deserialize("str", read_line())
    word2: str = deserialize("str", read_line())
    ans = Solution().closeStrings(word1, word2)

    print("\noutput:", serialize(ans))
