# Created by Jones at 2024/01/14 10:30
# leetgo: dev
# https://leetcode.cn/problems/find-beautiful-indices-in-the-given-array-ii/
# https://leetcode.cn/contest/weekly-contest-380/problems/find-beautiful-indices-in-the-given-array-ii/

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
def prefix_function(s):
    n = len(s)
    pi = [0] * n
    for i in range(1, n):
        j = pi[i - 1]
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j
    return pi


def find_occurrences(t, s):
    cur = s + "#" + t
    sz1, sz2 = len(t), len(s)
    ret = []
    lps = prefix_function(cur)
    for i in range(sz2 + 1, sz1 + sz2 + 1):
        if lps[i] == sz2:
            ret.append(i - 2 * sz2)
    return ret


class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        va = find_occurrences(s, a)
        vb = find_occurrences(s, b)
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
