# Created by Jones at 2023/11/26 10:30
# leetgo: dev
# https://leetcode.cn/problems/count-beautiful-substrings-ii/
# https://leetcode.cn/contest/weekly-contest-373/problems/count-beautiful-substrings-ii/

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
    def beautifulSubstrings(self, s: str, k: int) -> int:
        # (L/2) ** 2 % k == 0
        L = None
        for d in count(1):
            if d * d % (4 * k) == 0:
                L = d
                break
        assert L is not None

        s = [1 if ch in "aeiou" else -1 for ch in s]
        p = list(accumulate(s, initial=0))

        res = 0
        cnt = Counter()
        for i, s in enumerate(p):
            p = (s, i % L)
            res += cnt[p]
            cnt[p] += 1

        return res


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().beautifulSubstrings(s, k)

    print("\noutput:", serialize(ans))
