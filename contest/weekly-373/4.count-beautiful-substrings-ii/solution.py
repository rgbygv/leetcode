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
        k *= 2
        f = [False] * (k + 1)
        f[0] = True
        for i in range(1, k + 1):
            f[i] = i * i % k == 0

        s = [ch in "aeiou" for ch in s]

        # s[i..j] = 0 and (i-j)//2 ** 2 % k == 0

        ss = 0
        res = 0
        pre = defaultdict(lambda: defaultdict(int))
        if k == 1:
            pre[0][-1] = 1
        for i, ch in enumerate(s):
            x = 1 if ch else -1
            ss += x
            for j, c in pre[ss].items():
                if f[abs(i % k - j)]:
                    print(i, abs(i % k - j), pre[ss])
                    res += c
            pre[ss][i % k] += 1

        return res


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().beautifulSubstrings(s, k)

    print("\noutput:", serialize(ans))
