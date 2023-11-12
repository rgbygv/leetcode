# Created by Jones at 2023/11/12 10:30
# leetgo: dev
# https://leetcode.cn/problems/high-access-employees/
# https://leetcode.cn/contest/weekly-contest-371/problems/high-access-employees/

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
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        mp = defaultdict(list)
        for name, t in access_times:
            a, b = t[:2], t[2:]
            t = int(a) * 60 + int(b)
            mp[name].append(t)
        res = []
        for key in mp:
            v = sorted(mp[key])
            if any(v[i + 2] - v[i] < 60 for i in range(len(v) - 2)):
                res.append(key)
        return res


# @lc code=end

if __name__ == "__main__":
    access_times: List[List[str]] = deserialize("List[List[str]]", read_line())
    ans = Solution().findHighAccessEmployees(access_times)

    print("\noutput:", serialize(ans))
