# Created by Jones at 2024/01/13 14:11
# leetgo: dev
# https://leetcode.cn/problems/construct-string-with-repeat-limit/

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
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        cnt = Counter(s)
        st = sorted(cnt.items())

        res = []
        while st:
            a, cnt1 = st.pop()
            while cnt1 > repeatLimit and st:
                b, cnt2 = st.pop()
                res.append(a * repeatLimit)
                res.append(b)
                if cnt2 > 1:
                    st.append((b, cnt2 - 1))
                cnt1 -= repeatLimit
            res.append(a * min(cnt1, repeatLimit))
        return "".join(res)


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    repeatLimit: int = deserialize("int", read_line())
    ans = Solution().repeatLimitedString(s, repeatLimit)

    print("\noutput:", serialize(ans))
