# Created by Jones at 2024/01/12 13:30
# leetgo: dev
# https://leetcode.cn/problems/count-common-words-with-one-occurrence/

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


class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        cnt1 = Counter(words1)
        cnt2 = Counter(words2)

        return sum(v == 1 and cnt2[i] == 1 for i, v in cnt1.items())


# @lc code=end

if __name__ == "__main__":
    words1: List[str] = deserialize("List[str]", read_line())
    words2: List[str] = deserialize("List[str]", read_line())
    ans = Solution().countWords(words1, words2)

    print("\noutput:", serialize(ans))
