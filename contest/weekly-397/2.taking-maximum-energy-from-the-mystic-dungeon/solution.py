# Created by Jones at 2024/05/12 18:20
# leetgo: 1.4.7
# https://leetcode.cn/problems/taking-maximum-energy-from-the-mystic-dungeon/
# https://leetcode.cn/contest/weekly-contest-397/problems/taking-maximum-energy-from-the-mystic-dungeon/

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
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        """
        - `1 <= energy.length <= 10⁵`
        - `-1000 <= energy[i] <= 1000`
        - `1 <= k <= energy.length - 1`
        """

        def f(a: list[int]):
            return max(accumulate(a[::-1]))

        return max(f(energy[i::k]) for i in range(k))


# @lc code=end

if __name__ == "__main__":
    energy: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().maximumEnergy(energy, k)
    print("\noutput:", serialize(ans, "integer"))
