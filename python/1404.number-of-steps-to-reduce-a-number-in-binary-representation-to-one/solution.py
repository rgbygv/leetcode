# Created by Jones at 2024/05/29 13:09
# leetgo: 1.4.7
# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/

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
    def numSteps(self, s: str) -> int:
        res = 0
        n = len(s)
        carry = 0
        for i in range(n - 1, 0, -1):
            carry += int(s[i])
            if carry == 1:
                res += 2
            elif carry == 0:
                res += 1
                carry = 0
            else:
                res += 1
                carry = 1
        return res + carry


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().numSteps(s)
    print("\noutput:", serialize(ans, "integer"))
