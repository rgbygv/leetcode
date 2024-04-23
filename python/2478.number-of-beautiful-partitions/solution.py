# Created by Jones at 2024/04/23 16:29
# leetgo: 1.4.5
# https://leetcode.cn/problems/number-of-beautiful-partitions/

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
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        # - `1 <= k, minLength <= s.length <= 1000`
        # - `s` consists of the digits `'1'` to `'9'`.

        can = "2357"
        mod = int(1e9) + 7
        n = len(s)
        if k * minLength > n:  # can't split to k sub-str
            return 0
        if s[0] not in can or s[-1] in can:  # the first or last sub str is not satisfy
            return 0

        @cache
        def dfs(i: int, cnt: int, size: int):
            """we now in s[i], still need split `cnt`, and the rest need `size` of current sub_string"""
            if i == n:
                # have split to `cnt` str and split at n - 1
                # print(i, cnt, size)
                return int(cnt == 0 and size == minLength)
                # return int(cnt == 0 and size == 0)
            # if cnt == 1 and size == minLength:
            #     return int(s[i] in can)
            # try split here
            op1 = 0
            # still need handle the i+1 >= n
            if (
                cnt >= 1
                and size <= 1
                and s[i] not in can
                and (i + 1 == n or s[i + 1] in can)
            ):
                op1 = dfs(i + 1, cnt - 1, minLength)  # start a new sub str
            # don't split
            op2 = dfs(i + 1, cnt, max(size - 1, 0))  # the size <= 0 is equal to 0
            # op2 = dfs(i + 1, cnt, size - 1)
            # print(i, cnt, size, op1, op2)
            return (op1 + op2) % mod

        return dfs(0, k, minLength)


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    k: int = deserialize("int", read_line())
    minLength: int = deserialize("int", read_line())
    ans = Solution().beautifulPartitions(s, k, minLength)
    print("\noutput:", serialize(ans, "integer"))
