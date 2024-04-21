# Created by Jones at 2024/04/21 13:16
# leetgo: 1.4.5
# https://leetcode.cn/problems/count-the-number-of-special-characters-ii/
# https://leetcode.cn/contest/weekly-contest-394/problems/count-the-number-of-special-characters-ii/

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
    def numberOfSpecialChars(self, word: str) -> int:
        mp = defaultdict(list)
        for ch in word:
            mp[ch.upper()].append(ch)
        res = 0
        for ch, v in mp.items():
            if len(set(v)) == 2:
                try:
                    i = v.index(ch)
                    res += all(v[j] == ch for j in range(i, len(v)))
                except:
                    pass

        return res


# @lc code=end

if __name__ == "__main__":
    word: str = deserialize("str", read_line())
    ans = Solution().numberOfSpecialChars(word)
    print("\noutput:", serialize(ans, "integer"))
