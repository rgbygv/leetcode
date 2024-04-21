# Created by Jones at 2024/04/21 13:16
# leetgo: 1.4.5
# https://leetcode.cn/problems/count-the-number-of-special-characters-i/
# https://leetcode.cn/contest/weekly-contest-394/problems/count-the-number-of-special-characters-i/

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
    def numberOfSpecialChars(self, word: str) -> int:
        s = set(word)
        return sum(x.lower() in s and x.upper() in s for x in s) // 2


# @lc code=end

if __name__ == "__main__":
    word: str = deserialize("str", read_line())
    ans = Solution().numberOfSpecialChars(word)
    print("\noutput:", serialize(ans, "integer"))
