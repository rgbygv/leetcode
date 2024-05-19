# Created by Jones at 2024/05/19 15:06
# leetgo: 1.4.7
# https://leetcode.cn/problems/find-the-winner-of-an-array-game/

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
    def getWinner(self, arr: List[int], k: int) -> int:
        """
        - `2 <= arr.length <= 10⁵`
        - `1 <= arr[i] <= 10⁶`
        - `arr` contains **distinct** integers.
        - `1 <= k <= 10⁹`
        """
        n = len(arr)
        if k >= n:
            return max(arr)
        mx = max(arr)
        cnt = 0
        last = arr[0]
        for i in range(1, len(arr)):
            x = arr[i]
            if last > x:
                cnt += 1
            else:
                if x == mx:
                    return x
                last = x
                cnt = 1
            if cnt == k:
                return last
        return -1


# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().getWinner(arr, k)
    print("\noutput:", serialize(ans, "integer"))
