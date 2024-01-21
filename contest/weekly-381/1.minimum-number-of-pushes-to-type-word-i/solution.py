# Created by Jones at 2024/01/21 15:10
# leetgo: dev
# https://leetcode.cn/problems/minimum-number-of-pushes-to-type-word-i/
# https://leetcode.cn/contest/weekly-contest-381/problems/minimum-number-of-pushes-to-type-word-i/

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
    def minimumPushes(self, word: str) -> int:
        n = len(word)

        res = 0
        cnt = 1
        while n >= 8:
            res += 8 * cnt
            n -= 8
            cnt += 1
        res += n * cnt
        return res


# @lc code=end

if __name__ == "__main__":
    word: str = deserialize("str", read_line())
    ans = Solution().minimumPushes(word)

    print("\noutput:", serialize(ans))
