# Created by Jones at 2024/05/30 13:09
# leetgo: 1.4.7
# https://leetcode.cn/problems/find-longest-special-substring-that-occurs-thrice-ii/

from typing import *
from leetgo_py import *

from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from functools import cache, cmp_to_key, lru_cache, reduce
from heapq import heapify, heappop, heappush, heappushpop, heapreplace
from icecream import ic
from itertools import accumulate, chain, count, pairwise, zip_longest
from math import ceil, comb, floor, gcd, inf, isqrt, lcm, log2, perm, sqrt
from operator import xor
from pprint import pprint
from string import ascii_lowercase
from typing import List, Optional

# @lc code=begin


class Solution:
    def maximumLength(self, s: str) -> int:
        """
        - `3 <= s.length <= 5 * 10⁵`
        - `s` consists of only lowercase English letters.
        """
        mp = defaultdict(list)
        for i, ch in enumerate(s):
            mp[ch].append(i)

        res = -1

        for v in mp.values():
            if len(v) < 3:
                continue
            q = []
            n = len(v)
            i = 0
            while i < n:
                j = i + 1
                while j < n and v[j] == v[j - 1] + 1:
                    j += 1
                q.append(j - i)
                q.sort(reverse=True)
                if len(q) > 3:
                    q.pop()
                i = j

            # ans = max(q[0] - 2, q[1] - 1, q[2])
            res = max(res, q[0] - 2)
            if len(q) > 1:
                res = max(res, q[1] - 1)
                if q[0] > q[1]:
                    res = max(res, q[1])
                if len(q) > 2:
                    res = max(res, q[2])
        return res


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().maximumLength(s)
    print("\noutput:", serialize(ans, "integer"))
