# Created by Jones at 2024/03/10 13:54
# leetgo: 1.4.1
# https://leetcode.cn/problems/maximize-happiness-of-selected-children/
# https://leetcode.cn/contest/weekly-contest-388/problems/maximize-happiness-of-selected-children/

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
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()
        n = len(happiness)
        res = 0
        for i in range(k):
            res += max(0, happiness[n - 1 - i] - i)
        return res


# @lc code=end

if __name__ == "__main__":
    happiness: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().maximumHappinessSum(happiness, k)
    print("\noutput:", serialize(ans, "long"))
