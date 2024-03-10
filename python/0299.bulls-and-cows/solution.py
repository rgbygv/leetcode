# Created by Jones at 2024/03/10 12:05
# leetgo: 1.4.1
# https://leetcode.cn/problems/bulls-and-cows/

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
    def getHint(self, secret: str, guess: str) -> str:
        a = sum(x == y for x, y in zip(secret, guess))
        b = (Counter(secret) & Counter(guess)).total()

        return f"{a}A{b-a}B"


# @lc code=end

if __name__ == "__main__":
    secret: str = deserialize("str", read_line())
    guess: str = deserialize("str", read_line())
    ans = Solution().getHint(secret, guess)
    print("\noutput:", serialize(ans, "string"))
