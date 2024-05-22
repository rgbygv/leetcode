# Created by Jones at 2024/05/22 10:16
# leetgo: 1.4.7
# https://leetcode.com/problems/palindrome-partitioning/

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
    def partition(self, s: str) -> List[List[str]]:
        """
        - `1 <= s.length <= 16`
        - `s` contains only lowercase English letters.
        """
        n = len(s)

        res = []
        path = []

        def dfs(i: int):
            if i == n:
                res.append(path[:])
                return
            for j in range(i + 1, n + 1):
                cur = s[i:j]
                if cur == cur[::-1]:
                    path.append(cur)
                    dfs(j)
                    path.pop()

        dfs(0)
        return res


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().partition(s)
    print("\noutput:", serialize(ans, "string[][]"))
