# Created by Jones at 2023/11/05 12:08
# leetgo: dev
# https://leetcode.cn/problems/repeated-dna-sequences/

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
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        cnt = Counter()

        for i in range(10, len(s) + 1):
            cur = s[i - 10 : i]
            cnt[cur] += 1

        return [key for key, c in cnt.items() if c > 1]


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().findRepeatedDnaSequences(s)

    print("\noutput:", serialize(ans))
