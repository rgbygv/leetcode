# Created by Jones at 2023/10/19 14:08
# leetgo: dev
# https://leetcode.cn/problems/backspace-string-compare/

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
# from sortedcontainers import SortedList


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def f(s: str):
            st = []
            for ch in s:
                if ch == "#":
                    if st:
                        st.pop()
                else:
                    st.append(ch)
            return "".join(st)

        return f(s) == f(t)


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    t: str = deserialize("str", read_line())
    ans = Solution().backspaceCompare(s, t)

    print("\noutput:", serialize(ans))
