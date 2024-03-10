# Created by Jones at 2024/03/10 13:54
# leetgo: 1.4.1
# https://leetcode.cn/problems/apple-redistribution-into-boxes/
# https://leetcode.cn/contest/weekly-contest-388/problems/apple-redistribution-into-boxes/

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
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        s = sum(apple)
        capacity.sort(reverse=True)
        for i, x in enumerate(capacity, 1):
            if s <= x:
                return i
            s -= x
        return -1


# @lc code=end

if __name__ == "__main__":
    apple: List[int] = deserialize("List[int]", read_line())
    capacity: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minimumBoxes(apple, capacity)
    print("\noutput:", serialize(ans, "integer"))
