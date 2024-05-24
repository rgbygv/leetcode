# Created by Jones at 2024/05/24 14:22
# leetgo: 1.4.7
# https://leetcode.cn/problems/construct-the-lexicographically-largest-valid-sequence/

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
    def constructDistancedSequence(self, n: int) -> List[int]:
        """
        - `1 <= n <= 20`

        ```
        Input: n = 5
        Output: [5,3,1,4,3,5,2,4,2]
        ```
        """
        size = n * 2 - 1
        a = [0] * size

        def dfs(i: int):
            if i == size:
                return True
            if a[i] != 0:
                return dfs(i + 1)
            for x in range(n, 0, -1):
                if x in a:
                    continue
                gap = x if x != 1 else 0
                if i + gap < size and a[i + gap] == 0:
                    a[i] = a[i + gap] = x
                    if dfs(i + 1):
                        return True
                    a[i] = a[i + gap] = 0
            return False

        dfs(0)
        return a


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().constructDistancedSequence(n)
    print("\noutput:", serialize(ans, "integer[]"))
