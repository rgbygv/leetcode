# Created by Jones at 2024/06/02 13:46
# leetgo: 1.4.7
# https://leetcode.cn/problems/count-days-without-meetings/
# https://leetcode.cn/contest/weekly-contest-400/problems/count-days-without-meetings/

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
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        """
        - `1 <= days <= 10⁹`
        - `1 <= meetings.length <= 10⁵`
        - `meetings[i].length == 2`
        - `1 <= meetings[i][0] <= meetings[i][1] <= days`
        """
        d = defaultdict(int)
        for x, y in meetings:
            d[x] += 1
            d[y] -= 1

        res = 0
        cnt = 0
        q = sorted(d.keys())
        if q[0] > 1:
            res += q[0] - 1
        if q[-1] < days:
            res += days - q[-1]

        for x, y in pairwise(q):
            cnt += d[x]
            if cnt == 0:
                res += y - x - 1
        return res


# @lc code=end

if __name__ == "__main__":
    days: int = deserialize("int", read_line())
    meetings: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().countDays(days, meetings)
    print("\noutput:", serialize(ans, "integer"))
