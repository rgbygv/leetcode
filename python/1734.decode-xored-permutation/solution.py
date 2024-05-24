# Created by Jones at 2024/05/24 15:13
# leetgo: 1.4.7
# https://leetcode.cn/problems/decode-xored-permutation/

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
    def decode(self, encoded: List[int]) -> List[int]:
        """
        ```
        Input: encoded = [6,5,4,6]
        Output: [2,4,1,5,3]
        ```
        e[i] = a[i] ^ a[i+1]
        f[i] = e[i] ^ e[i-1] = a[0] ^ a[i]

        """
        n = len(encoded) + 1
        s = 0
        x = 0
        for e in encoded:
            s ^= e
            x ^= s
        for i in range(1, n + 1):
            x ^= i
        res = [x]
        for e in encoded:
            x ^= e
            res.append(x)

        return res


# @lc code=end

if __name__ == "__main__":
    encoded: List[int] = deserialize("List[int]", read_line())
    ans = Solution().decode(encoded)
    print("\noutput:", serialize(ans, "integer[]"))
