# Created by Jones at 2024/01/14 10:30
# leetgo: dev
# https://leetcode.cn/problems/find-beautiful-indices-in-the-given-array-i/
# https://leetcode.cn/contest/weekly-contest-380/problems/find-beautiful-indices-in-the-given-array-i/

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
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        n = len(s)

        def f(a):
            m = len(a)
            v = []
            for i in range(n - m + 1):
                if s[i : i + m] == a:
                    v.append(i)
            return v

        va = f(a)
        vb = f(b)

        res = []
        for i in va:
            j = bisect_left(vb, i)
            ok = False
            if j < len(vb) and vb[j] - i <= k:
                ok = True
            if j > 0 and i - vb[j - 1] <= k:
                ok = True
            if ok:
                res.append(i)
        return res


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    a: str = deserialize("str", read_line())
    b: str = deserialize("str", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().beautifulIndices(s, a, b, k)

    print("\noutput:", serialize(ans))
