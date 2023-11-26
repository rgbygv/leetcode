# Created by Jones at 2023/11/25 22:30
# leetgo: dev
# https://leetcode.cn/problems/find-words-containing-character/
# https://leetcode.cn/contest/biweekly-contest-118/problems/find-words-containing-character/

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
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [i for i, w in enumerate(words) if x in w]


# @lc code=end

if __name__ == "__main__":
    words: List[str] = deserialize("List[str]", read_line())
    x: str = deserialize("str", read_line())
    ans = Solution().findWordsContaining(words, x)

    print("\noutput:", serialize(ans))
