# Created by Bob at 2023/12/31 15:57
# leetgo: dev
# https://leetcode.cn/problems/find-longest-special-substring-that-occurs-thrice-ii/
# https://leetcode.cn/contest/weekly-contest-378/problems/find-longest-special-substring-that-occurs-thrice-ii/

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
    def maximumLength(self, s: str) -> int:
        mp = defaultdict(list)
        for i, ch in enumerate(s):
            mp[ch].append(i)

        res = -1
        for v in mp.values():
            if len(v) < 3:
                continue
            q = []
            pre = v[0] - 1
            cnt = 0
            for x in v:
                if x == pre + 1:
                    cnt += 1
                else:
                    if cnt:
                        q.append(cnt)
                    cnt = 1
                pre = x
            q.append(cnt)

            m = len(q)
            q.sort()
            l, r = 1, int(5e5) + 1
            while l < r:
                mid = (l + r) >> 1

                def check(mid):
                    j = bisect_left(q, mid)
                    cnt = 0
                    for i in range(j, m):
                        cnt += q[i] - mid + 1
                    return cnt >= 3

                if check(mid):
                    l = mid + 1
                else:
                    r = mid
            # print(q)
            res = max(res, l - 1)

        return res


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().maximumLength(s)

    print("\noutput:", serialize(ans))
