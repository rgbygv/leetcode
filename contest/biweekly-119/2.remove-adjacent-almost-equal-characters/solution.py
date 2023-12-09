# Created by Jones at 2023/12/09 22:30
# leetgo: dev
# https://leetcode.cn/problems/remove-adjacent-almost-equal-characters/
# https://leetcode.cn/contest/biweekly-contest-119/problems/remove-adjacent-almost-equal-characters/

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
    def removeAlmostEqualCharacters(self, word: str) -> int:
        i = 0
        n = len(word)

        res = 0
        while i < n:
            if i + 1 < n and abs(ord(word[i + 1]) - ord(word[i])) <= 1:
                res += 1
                i += 2
            else:
                i += 1
        return res


# @lc code=end

if __name__ == "__main__":
    word: str = deserialize("str", read_line())
    ans = Solution().removeAlmostEqualCharacters(word)

    print("\noutput:", serialize(ans))
