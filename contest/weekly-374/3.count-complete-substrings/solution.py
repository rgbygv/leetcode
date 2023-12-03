# Created by Jones at 2023/12/03 10:30
# leetgo: dev
# https://leetcode.cn/problems/count-complete-substrings/
# https://leetcode.cn/contest/weekly-contest-374/problems/count-complete-substrings/

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
    def countCompleteSubstrings(self, word: str, k: int) -> int:
        cnt = Counter()
        @cache
        def check(a,b):
            return abs(ord(a) - ord(b)) <= 2
        for c
        
        



# @lc code=end

if __name__ == "__main__":
    word: str = deserialize("str", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().countCompleteSubstrings(word, k)

    print("\noutput:", serialize(ans))
