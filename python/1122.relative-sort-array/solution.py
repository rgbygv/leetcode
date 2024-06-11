# Created by Jones at 2024/06/11 15:10
# leetgo: 1.4.7
# https://leetcode.com/problems/relative-sort-array/

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
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        """
        - `1 <= arr1.length, arr2.length <= 1000`
        - `0 <= arr1[i], arr2[i] <= 1000`
        - All the elements of `arr2` are **distinct**.
        - Each `arr2[i]` is in `arr1`.
        """
        rank = defaultdict(lambda: inf)
        n = len(arr2)
        for i, x in enumerate(arr2):
            rank[x] = i

        for x in arr1:
            if x not in rank:
                rank[x] = x + n

        return sorted(arr1, key=lambda x: rank[x])


# @lc code=end

if __name__ == "__main__":
    arr1: List[int] = deserialize("List[int]", read_line())
    arr2: List[int] = deserialize("List[int]", read_line())
    ans = Solution().relativeSortArray(arr1, arr2)
    print("\noutput:", serialize(ans, "integer[]"))
