# Created by Jones at 2024/05/09 15:19
# leetgo: 1.4.6
# https://leetcode.cn/problems/best-team-with-no-conflicts/

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
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        """
        - `1 <= scores.length, ages.length <= 1000`
        - `scores.length == ages.length`
        - `1 <= scores[i] <= 10⁶`
        - `1 <= ages[i] <= 1000`
        """
        q = sorted(zip(ages, scores))
        n = len(q)
        f = [0] * (n + 1)

        for i, (age, score) in enumerate(q, 1):
            # select player[i]
            op1 = 0
            for j in range(1, i):
                if not (q[j - 1][0] < age and q[j - 1][1] > score):
                    op1 = max(op1, f[j])
            op1 += score
            # don't select player[i]
            f[i] = op1
        # ic(q, f)
        return max(f)


# @lc code=end

if __name__ == "__main__":
    scores: List[int] = deserialize("List[int]", read_line())
    ages: List[int] = deserialize("List[int]", read_line())
    ans = Solution().bestTeamScore(scores, ages)
    print("\noutput:", serialize(ans, "integer"))
