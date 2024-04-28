# Created by Jones at 2024/04/28 19:03
# leetgo: 1.4.5
# https://leetcode.cn/problems/convert-to-base-2/

from typing import *
from leetgo_py import *

from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from copy import deepcopy
from functools import cache, cmp_to_key, lru_cache, reduce
from heapq import heapify, heappop, heappush, heappushpop, heapreplace
from itertools import accumulate, chain, count, pairwise, zip_longest
from math import ceil, comb, floor, gcd, inf, isqrt, log2, perm, sqrt
from operator import xor
from pprint import pprint
from string import ascii_lowercase
from typing import List, Optional

# @lc code=begin


class Solution:
    def baseNeg2(self, x: int) -> str:
        n = 31
        bits = [0] * n

        for i in range(n - 1):
            if x >> i & 1:
                # we should make 2**i
                if i & 1 == 0:
                    bits[i] += 1
                else:
                    bits[i] += 1
                    bits[i + 1] += 1
        # print(bits)
        for i in range(n):
            if bits[i] >= 2:
                t = bits[i] // 2
                bits[i] &= 1
                if i + 1 < n:
                    bits[i + 1] += t
                    if i + 2 < n:
                        bits[i + 2] += t

        res = "".join(map(str, bits[::-1])).lstrip("0")
        if not res:
            return "0"
        return res


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().baseNeg2(n)
    print("\noutput:", serialize(ans, "string"))
