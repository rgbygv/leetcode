# Created by Jones at 2024/01/11 20:02
# leetgo: dev
# https://leetcode.cn/problems/minimum-additions-to-make-valid-string/

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
    def addMinimum(self, word: str) -> int:
        s = "abc"

        mp = {v: i for i, v in enumerate(s)}
        last = "c"
        res = 0
        for ch in word:
            if last != s[(mp[ch]) - 1]:
                # if ch == "a":
                #     res += 1 if last == "b" else 2
                # elif ch == "b":
                #     res += 1 if last == "c" else 2
                # else:
                #     res += 1 if last == "a" else 2
                res += 1 + (ch == last)

            last = ch
        if last != "c":
            res += 2 - mp[last]
    
        return res


# @lc code=end

if __name__ == "__main__":
    word: str = deserialize("str", read_line())
    ans = Solution().addMinimum(word)

    print("\noutput:", serialize(ans))
