# Created by Jones at 2023/12/24 22:16
# leetgo: dev
# https://leetcode.cn/problems/minimum-cost-to-convert-string-ii/
# https://leetcode.cn/contest/weekly-contest-377/problems/minimum-cost-to-convert-string-ii/

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
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:

# @lc code=end

if __name__ == "__main__":
    source: str = deserialize("str", read_line())
    target: str = deserialize("str", read_line())
    original: List[str] = deserialize("List[str]", read_line())
    changed: List[str] = deserialize("List[str]", read_line())
    cost: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minimumCost(source, target, original, changed, cost)

    print("\noutput:", serialize(ans))
