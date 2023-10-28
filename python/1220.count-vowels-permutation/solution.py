# Created by Jones at 2023/10/28 13:13
# leetgo: dev
# https://leetcode.cn/problems/count-vowels-permutation/

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
    def countVowelPermutation(self, n: int) -> int:
        mod = 10**9 + 7
        mp = {"": "aeiou", "a": "e", "e": "ai", "i": "aeou", "o": "iu", "u": "a"}

        @cache
        def dfs(i: int, last: str):
            if i == n:
                return 1

            res = 0
            for next_ch in mp[last]:
                res += dfs(i + 1, next_ch)

            return res % mod

        return dfs(0, "")


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().countVowelPermutation(n)

    print("\noutput:", serialize(ans))
