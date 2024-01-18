# Created by Jones at 2024/01/18 14:33
# leetgo: dev
# https://leetcode.cn/problems/removing-minimum-number-of-magic-beans/

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
    def minimumRemoval(self, beans: List[int]) -> int:
        s = sum(beans)

        heapify(beans)
        # print(beans)

        res = inf
        n = len(beans)
        pre = 0
        for x in range(max(beans) + 1):
            while beans and beans[0] < x:
                b = heappop(beans)
                pre += b
                n -= 1
                s -= b
            cur = pre + s - x * n
            res = min(res, cur)
            # print(x, cur, res)
        return res


# @lc code=end

if __name__ == "__main__":
    beans: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minimumRemoval(beans)

    print("\noutput:", serialize(ans))
