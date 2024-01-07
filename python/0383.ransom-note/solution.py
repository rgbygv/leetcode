# Created by Jones at 2024/01/07 18:42
# leetgo: dev
# https://leetcode.cn/problems/ransom-note/

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
from string import ascii_lowercase
from typing import List, Optional

# @lc code=begin


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return Counter(magazine) >= Counter(ransomNote)


# @lc code=end

if __name__ == "__main__":
    ransomNote: str = deserialize("str", read_line())
    magazine: str = deserialize("str", read_line())
    ans = Solution().canConstruct(ransomNote, magazine)

    print("\noutput:", serialize(ans))
