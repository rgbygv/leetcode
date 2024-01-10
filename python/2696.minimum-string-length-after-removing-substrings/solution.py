# Created by Jones at 2024/01/10 11:14
# leetgo: dev
# https://leetcode.cn/problems/minimum-string-length-after-removing-substrings/

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
    def minLength(self, s: str) -> int:
        mp = {"D": "C", "B": "A"}
        st = []

        for ch in s:
            if st and st[-1] == mp.get(ch, None):
                st.pop()
            else:
                st.append(ch)

        return len(st)


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().minLength(s)

    print("\noutput:", serialize(ans))
