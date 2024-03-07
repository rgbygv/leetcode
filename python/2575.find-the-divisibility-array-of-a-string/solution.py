# Created by Jones at 2024/03/07 13:05
# leetgo: 1.4.1
# https://leetcode.cn/problems/find-the-divisibility-array-of-a-string/

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
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        n = len(word)
        res = [0] * n
        s = 0
        for i, x in enumerate(word):
            s = s * 10 + int(x)
            s %= m
            if s == 0:
                res[i] = 1
        return res


# @lc code=end

if __name__ == "__main__":
    word: str = deserialize("str", read_line())
    m: int = deserialize("int", read_line())
    ans = Solution().divisibilityArray(word, m)
    print("\noutput:", serialize(ans, "integer[]"))
