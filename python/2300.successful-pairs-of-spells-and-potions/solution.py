# Created by Jones at 2023/11/10 13:53
# leetgo: dev
# https://leetcode.cn/problems/successful-pairs-of-spells-and-potions/

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
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        potions.sort()
        n = len(potions)
        res = []
        for x in spells:
            need = (success + x - 1) // x
            i = bisect_left(potions, need)
            res.append(n - i)
        return res


# @lc code=end

if __name__ == "__main__":
    spells: List[int] = deserialize("List[int]", read_line())
    potions: List[int] = deserialize("List[int]", read_line())
    success: int = deserialize("int", read_line())
    ans = Solution().successfulPairs(spells, potions, success)

    print("\noutput:", serialize(ans))
