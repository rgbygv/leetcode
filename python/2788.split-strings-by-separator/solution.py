# Created by Jones at 2024/01/20 13:14
# leetgo: dev
# https://leetcode.cn/problems/split-strings-by-separator/

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
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        res = []
        for w in words:
            for s in w.split(sep=separator):
                if s:
                    res.append(s)
        return res


# @lc code=end

if __name__ == "__main__":
    words: List[str] = deserialize("List[str]", read_line())
    separator: str = deserialize("str", read_line())
    ans = Solution().splitWordsBySeparator(words, separator)

    print("\noutput:", serialize(ans))
