# Created by Jones at 2023/12/03 10:30
# leetgo: dev
# https://leetcode.cn/problems/count-complete-substrings/
# https://leetcode.cn/contest/weekly-contest-374/problems/count-complete-substrings/

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
    def countCompleteSubstrings(self, word: str, k: int) -> int:
        a = [ord(ch) - ord("a") for ch in word]

        def f(v):
            res = 0
            n = len(v)
            for i in range(1, 27):
                if k * i > n:
                    break
                m = k * i
                cnt = [0] * 26
                for j in range(m - 1):
                    cnt[v[j]] += 1
                for j in range(m - 1, n):
                    cnt[v[j]] += 1
                    if all(x == 0 or x == k for x in cnt):
                        res += 1
                    cnt[v[j - (m - 1)]] -= 1

            return res

        i = 0
        n = len(a)
        res = 0
        while i < n:
            j = i + 1
            while j < n and abs(a[j] - a[j - 1]) <= 2:
                j += 1
            res += f(a[i:j])
            i = j
        return res


# @lc code=end

if __name__ == "__main__":
    word: str = deserialize("str", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().countCompleteSubstrings(word, k)

    print("\noutput:", serialize(ans))
