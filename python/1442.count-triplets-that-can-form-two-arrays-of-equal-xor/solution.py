# Created by Jones at 2024/05/30 13:18
# leetgo: 1.4.7
# https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/

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
    def countTriplets(self, arr: List[int]) -> int:
        """
        - `1 <= arr.length <= 300`
        - `1 <= arr[i] <= 10⁸`
        """

        res = 0
        for i, x in enumerate(arr):
            mask = x
            for j in range(i - 1, -1, -1):
                mask ^= arr[j]
                if mask == 0:
                    # ic(j, i)
                    res += i - j
        return res

        # wrong
        mp = {}
        mp[0] = 0
        mask = 0
        res = 0
        for i, x in enumerate(arr, 1):
            mask ^= x
            # xor(a[i..k]) == 0 and k-i>=1
            if mask == 0:
                res += i - 1
                continue

            if mask in mp:
                j = mp[mask]
                res += i - j - 1
            else:
                mp[mask] = i
        return res


# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    ans = Solution().countTriplets(arr)
    print("\noutput:", serialize(ans, "integer"))
