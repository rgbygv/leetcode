# Created by Jones at 2023/10/28 22:30
# leetgo: dev
# https://leetcode.cn/problems/minimum-number-of-changes-to-make-binary-string-beautiful/
# https://leetcode.cn/contest/biweekly-contest-116/problems/minimum-number-of-changes-to-make-binary-string-beautiful/

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
    def minChanges(self, s: str) -> int:
        n = len(s)
        res = 0
        for i in range(0, n, 2):
            if s[i] != s[i + 1]:
                res += 1

        return res


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().minChanges(s)

    print("\noutput:", serialize(ans))
