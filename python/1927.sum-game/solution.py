# Created by Jones at 2024/05/30 14:31
# leetgo: 1.4.7
# https://leetcode.cn/problems/sum-game/

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
    def sumGame(self, num: str) -> bool:
        n = len(num)
        cnt = 0
        s = 0
        for i, ch in enumerate(num):
            if i < (n >> 1):
                if ch == "?":
                    cnt += 1
                else:
                    s += int(ch)
            else:
                if ch == "?":
                    cnt -= 1
                else:
                    s -= int(ch)

        # if cnt == 0:
        #     return s != 0
        # if s >= 0 and cnt > 0 or s <= 0 and cnt < 0:
        #     return True
        # s, cnt = abs(s), abs(cnt)
        if cnt & 1:
            return True
        return 9 * cnt // 2 + s != 0


# @lc code=end

if __name__ == "__main__":
    num: str = deserialize("str", read_line())
    ans = Solution().sumGame(num)
    print("\noutput:", serialize(ans, "boolean"))
