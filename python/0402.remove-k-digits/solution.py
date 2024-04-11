# Created by Jones at 2024/04/11 12:59
# leetgo: 1.4.5
# https://leetcode.com/problems/remove-k-digits/

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
    def removeKdigits(self, num: str, k: int) -> str:
        st = []
        for ch in num:
            # can delete char
            while k > 0 and st and st[-1] > ch:
                k -= 1
                st.pop()
            st.append(ch)

        # st is ascending, and we move the last k chars
        st = st[: len(st) - k]

        return "".join(st).lstrip("0").ljust(1, "0")


# @lc code=end

if __name__ == "__main__":
    num: str = deserialize("str", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().removeKdigits(num, k)
    print("\noutput:", serialize(ans, "string"))
