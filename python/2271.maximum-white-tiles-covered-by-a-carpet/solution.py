# Created by Jones at 2024/06/03 15:04
# leetgo: 1.4.7
# https://leetcode.cn/problems/maximum-white-tiles-covered-by-a-carpet/

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
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        tiles.sort()
        n = len(tiles)
        res = 0
        l = 0
        s = 0
        for r in range(n):
            s += tiles[r][1] - tiles[r][0] + 1
            while tiles[r][1] - tiles[l][1] + 1 > carpetLen:
                s -= tiles[l][1] - tiles[l][0] + 1
                l += 1
            res = max(res, s - max(0, (tiles[r][1] - tiles[l][0] + 1) - carpetLen))
        return res


# @lc code=end

if __name__ == "__main__":
    tiles: List[List[int]] = deserialize("List[List[int]]", read_line())
    carpetLen: int = deserialize("int", read_line())
    ans = Solution().maximumWhiteTiles(tiles, carpetLen)
    print("\noutput:", serialize(ans, "integer"))
