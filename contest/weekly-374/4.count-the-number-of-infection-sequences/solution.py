# Created by Jones at 2023/12/03 10:30
# leetgo: dev
# https://leetcode.cn/problems/count-the-number-of-infection-sequences/
# https://leetcode.cn/contest/weekly-contest-374/problems/count-the-number-of-infection-sequences/

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
mod = 10**9 + 7

N = 10**5 + 1
f = [1] * N
for i in range(1, N):
    f[i] = i * f[i - 1] % mod


def inv(x):
    return pow(x, mod - 2, mod)


def my_comb(x, y):
    # f(x..x-y) / f(y..0)
    return f[x] * inv(f[x - y]) % mod * inv(f[y]) % mod


class Solution:
    def numberOfSequence(self, n: int, sick: List[int]) -> int:
        left = sick[0] - 0
        right = n - 1 - sick[-1]
        p = []
        s = n - len(sick)

        for a in (left, right):
            if a != 0:
                p.append((a, False))

        for x, y in pairwise(sick):
            a = y - x - 1
            if a != 0:
                p.append((a, True))
        res = 1
        for x, t in p:
            if t:
                res = my_comb(s, x) * res * (pow(2, x - 1, mod)) % mod
            else:
                res = my_comb(s, x) * res % mod
            s -= x
        return (res) % mod


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    sick: List[int] = deserialize("List[int]", read_line())
    ans = Solution().numberOfSequence(n, sick)

    print("\noutput:", serialize(ans))
