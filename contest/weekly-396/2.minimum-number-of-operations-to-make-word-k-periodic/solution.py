# Created by Jones at 2024/05/05 20:55
# leetgo: 1.4.6
# https://leetcode.cn/problems/minimum-number-of-operations-to-make-word-k-periodic/
# https://leetcode.cn/contest/weekly-contest-396/problems/minimum-number-of-operations-to-make-word-k-periodic/

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
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        n = len(word)
        cnt = Counter(word[i : i + k] for i in range(0, n, k))
        return n // k - max(cnt.values())


# @lc code=end

if __name__ == "__main__":
    word: str = deserialize("str", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().minimumOperationsToMakeKPeriodic(word, k)
    print("\noutput:", serialize(ans, "integer"))
