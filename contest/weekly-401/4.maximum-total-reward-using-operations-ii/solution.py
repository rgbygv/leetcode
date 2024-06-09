# Created by Jones at 2024/06/09 20:59
# leetgo: 1.4.7
# https://leetcode.cn/problems/maximum-total-reward-using-operations-ii/
# https://leetcode.cn/contest/weekly-contest-401/problems/maximum-total-reward-using-operations-ii/

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
from sortedcontainers import SortedList


class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        """
        - `1 <= rewardValues.length <= 5 * 10⁴`
        - `1 <= rewardValues[i] <= 5 * 10⁴`
        """
        a = sorted(set(rewardValues))
        mx = 2 * a[-1]
        can = set([0])
        ban = SortedList(range(1, mx))

        res = a[-1]
        for x in a:
            i = ban.bisect_left(x)
            j = ban.bisect_left(2 * x)
            if j - i <= len(ban):
                to_del = []
                for k in range(i, j):
                    if ban[k] - x in can:
                        res = max(res, ban[k])
                        can.add(ban[k])
                        to_del.append(ban[k])
                for x in to_del:
                    ban.remove(x)
            else:
                ok = []
                for y in can:
                    if y < x:
                        res = max(res, y + x)
                        ok.append(y + x)
                for key in ok:
                    can.add(key)
                    ban.remove(key)

        return res


# @lc code=end

if __name__ == "__main__":
    rewardValues: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxTotalReward(rewardValues)
    print("\noutput:", serialize(ans, "integer"))
