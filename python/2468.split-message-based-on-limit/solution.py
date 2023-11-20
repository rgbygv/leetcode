# Created by Jones at 2023/11/20 16:10
# leetgo: dev
# https://leetcode.cn/problems/split-message-based-on-limit/

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
    def splitMessage(self, message: str, limit: int) -> List[str]:
        if limit < 6:
            return []
        l = 1
        n = len(message)

        f = [0] * (n + 1)

        def cal(i):
            return n + f[i] + (len(str(i)) + 3) * i

        l = -1

        for i in range(1, n + 1):
            f[i] = len(str(i)) + f[i - 1]
            size = cal(i)
            if limit * (i - 1) < size <= limit * i:
                l = i
                break

        if l == -1:
            return []
        size = cal(l)
        fix = len(str(l)) + 3
        res = []
        i = 0
        for idx in range(1, l + 1):
            cur = len(str(idx)) + fix
            j = limit - cur
            res.append(f"{message[i:i+j]}<{idx}/{l}>")
            i += j

        return res


# @lc code=end

if __name__ == "__main__":
    message: str = deserialize("str", read_line())
    limit: int = deserialize("int", read_line())
    ans = Solution().splitMessage(message, limit)

    print("\noutput:", serialize(ans))
