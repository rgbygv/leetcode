# Created by Jones at 2024/06/09 20:59
# leetgo: 1.4.7
# https://leetcode.cn/problems/maximum-total-reward-using-operations-i/
# https://leetcode.cn/contest/weekly-contest-401/problems/maximum-total-reward-using-operations-i/

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
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        """
        - `1 <= rewardValues.length <= 2000`
        - `1 <= rewardValues[i] <= 2000`
        """
        a = sorted(set(rewardValues))
        n = len(a)

        @cache
        def dfs(i: int, s: int) -> int:
            if i == n:
                return s
            res = 0
            # choose i
            if a[i] > s:
                res = max(res, dfs(i + 1, s + a[i]))
            # don't choose i
            j = bisect_left(a, s, lo=i + 1)
            res = max(res, dfs(j, s))
            return res

        res = dfs(0, 0)
        dfs.cache_clear()
        return res


# @lc code=end

if __name__ == "__main__":
    rewardValues: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxTotalReward(rewardValues)
    print("\noutput:", serialize(ans, "integer"))
