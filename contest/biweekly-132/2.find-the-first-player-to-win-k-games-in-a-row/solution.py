# Created by Jones at 2024/06/10 13:09
# leetgo: 1.4.7
# https://leetcode.cn/problems/find-the-first-player-to-win-k-games-in-a-row/
# https://leetcode.cn/contest/biweekly-contest-132/problems/find-the-first-player-to-win-k-games-in-a-row/

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
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        """
        - `n == skills.length`
        - `2 <= n <= 10⁵`
        - `1 <= k <= 10⁹`
        - `1 <= skills[i] <= 10⁶`
        - All integers in `skills` are unique.
        """
        mx = max(skills)
        n = len(skills)
        if k >= n - 1:
            return skills.index(mx)

        last = 0
        cnt = 0
        for i in range(1, n):
            x = skills[i]
            if x > skills[last]:
                cnt = 1
                last = i
            else:
                cnt += 1
            if cnt >= k:
                return last
        return skills.index(mx)


# @lc code=end

if __name__ == "__main__":
    skills: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().findWinningPlayer(skills, k)
    print("\noutput:", serialize(ans, "integer"))
