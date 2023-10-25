# Created by Jones at 2023/10/25 09:58
# leetgo: dev
# https://leetcode.cn/problems/k-th-symbol-in-grammar/

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
    def kthGrammar(self, n: int, k: int) -> int:
        def dfs(n, k):
            if n == 1:
                return 0

            pre = dfs(n - 1, k >> 1)
            if pre == 1:
                return 1 if k & 1 == 0 else 0
            return 0 if k & 1 == 0 else 1

        return dfs(n, k - 1)


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().kthGrammar(n, k)

    print("\noutput:", serialize(ans))
