# Created by Jones at 2024/06/02 12:47
# leetgo: 1.4.7
# https://leetcode.cn/problems/stone-game-ix/

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
    def stoneGameIX(self, stones: List[int]) -> bool:
        cnt = [0] * 3

        for x in stones:
            cnt[x % 3] += 1
        cnt.reverse()
        ic(cnt)

        if cnt[0] == cnt[1] == 0:
            return False
        flg = bool(cnt[2] & 1)
        if cnt[0] == 0 or cnt[1] == 0:
            return flg if max(cnt[:2]) >= 3 else False
        if cnt[0] == 1 or cnt[1] == 1:
            return not flg
        diff = abs(cnt[0] - cnt[1])
        return flg if diff >= 3 else False


# @lc code=end

if __name__ == "__main__":
    stones: List[int] = deserialize("List[int]", read_line())
    ans = Solution().stoneGameIX(stones)
    print("\noutput:", serialize(ans, "boolean"))
