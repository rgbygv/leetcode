# Created by Jones at 2024/01/09 12:13
# leetgo: dev
# https://leetcode.cn/problems/extra-characters-in-a-string/

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


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dic = set(dictionary)

        n = len(s)

        @cache
        def dfs(i: int):
            res = n - i
            for j in range(i + 1, n + 1):
                res = min(res, j - i + dfs(j))
                if s[i:j] in dic:
                    res = min(res, dfs(j))
            # print(i, res)
            return res

        return dfs(0)


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    dictionary: List[str] = deserialize("List[str]", read_line())
    ans = Solution().minExtraChar(s, dictionary)

    print("\noutput:", serialize(ans))
