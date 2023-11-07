# Created by Jones at 2023/11/07 14:53
# leetgo: dev
# https://leetcode.cn/problems/count-the-number-of-vowel-strings-in-range/

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
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        vow = "aeiou"
        return sum(
            words[i][0] in vow and words[i][-1] in vow for i in range(left, right + 1)
        )


# @lc code=end

if __name__ == "__main__":
    words: List[str] = deserialize("List[str]", read_line())
    left: int = deserialize("int", read_line())
    right: int = deserialize("int", read_line())
    ans = Solution().vowelStrings(words, left, right)

    print("\noutput:", serialize(ans))
