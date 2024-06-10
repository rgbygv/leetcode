# Created by Jones at 2024/06/10 13:09
# leetgo: 1.4.7
# https://leetcode.cn/problems/clear-digits/
# https://leetcode.cn/contest/biweekly-contest-132/problems/clear-digits/

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
    def clearDigits(self, s: str) -> str:
        st = []
        for ch in s:
            if ch.isdigit():
                if st:
                    st.pop()
            else:
                st.append(ch)
        return "".join(st)


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().clearDigits(s)
    print("\noutput:", serialize(ans, "string"))
