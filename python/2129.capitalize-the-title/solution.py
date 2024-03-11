# Created by Jones at 2024/03/11 13:08
# leetgo: 1.4.1
# https://leetcode.cn/problems/capitalize-the-title/

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
    def capitalizeTitle(self, title: str) -> str:
        words = title.split()
        for i,w in enumerate(words):
            if len(w)>2:
                words[i] = w[0].upper() + w[1:].lower()
            else:
                words[i] = w.lower()
        return " ".join(words)

# @lc code=end

if __name__ == "__main__":
    title: str = deserialize("str", read_line())
    ans = Solution().capitalizeTitle(title)
    print("\noutput:", serialize(ans, "string"))
