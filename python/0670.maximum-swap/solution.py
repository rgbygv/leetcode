# Created by Jones at 2024/01/22 15:04
# leetgo: dev
# https://leetcode.cn/problems/maximum-swap/

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
    def maximumSwap(self, num: int) -> int:
        s = str(num)
        n = len(s)

        for i in range(n - 1):
            mx = max(s[i + 1 :])
            if mx > s[i]:
                j = s.rindex(mx)
                s = list(s)
                s[i], s[j] = s[j], s[i]
                s = "".join(s)
                break
        return int(s)


# @lc code=end

if __name__ == "__main__":
    num: int = deserialize("int", read_line())
    ans = Solution().maximumSwap(num)

    print("\noutput:", serialize(ans))
