# Created by Jones at 2024/06/02 13:46
# leetgo: 1.4.7
# https://leetcode.cn/problems/minimum-number-of-chairs-in-a-waiting-room/
# https://leetcode.cn/contest/weekly-contest-400/problems/minimum-number-of-chairs-in-a-waiting-room/

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
    def minimumChairs(self, s: str) -> int:
        res = 0
        cnt = 0
        for ch in s:
            cnt += 1 if ch == "E" else -1
            res = max(res, cnt)
        return res


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().minimumChairs(s)
    print("\noutput:", serialize(ans, "integer"))
