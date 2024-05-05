# Created by Jones at 2024/05/05 20:55
# leetgo: 1.4.6
# https://leetcode.cn/problems/valid-word/
# https://leetcode.cn/contest/weekly-contest-396/problems/valid-word/

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
    def isValid(self, word: str) -> bool:
        v = "aeiou"
        v = set(v + v.upper())

        nv = set(ascii_lowercase + ascii_lowercase.upper()) - v
        return (
            len(word) >= 3
            and all(ch not in word for ch in "@#$")
            and any(ch in v for ch in word)
            and any(ch in nv for ch in word)
        )


# @lc code=end

if __name__ == "__main__":
    word: str = deserialize("str", read_line())
    ans = Solution().isValid(word)
    print("\noutput:", serialize(ans, "boolean"))
