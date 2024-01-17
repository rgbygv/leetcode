# Created by Jones at 2024/01/17 14:53
# leetgo: dev
# https://leetcode.cn/problems/find-maximum-number-of-string-pairs/

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
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        seen = set()
        res = 0
        for w in words:
            rev = w[::-1]
            if rev in seen:
                res += 1
                seen.remove(rev)
            else:
                seen.add(w)

        return res


# @lc code=end

if __name__ == "__main__":
    words: List[str] = deserialize("List[str]", read_line())
    ans = Solution().maximumNumberOfStringPairs(words)

    print("\noutput:", serialize(ans))
