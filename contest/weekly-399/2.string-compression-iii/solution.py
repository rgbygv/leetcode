# Created by Jones at 2024/05/30 19:14
# leetgo: 1.4.7
# https://leetcode.cn/problems/string-compression-iii/
# https://leetcode.cn/contest/weekly-contest-399/problems/string-compression-iii/

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
    def compressedString(self, word: str) -> str:
        n = len(word)
        s = ""
        i = 0
        while i < n:
            j = i + 1
            while j < n and word[j] == word[i]:
                j += 1

            a, b = divmod(j - i, 9)
            if a:
                s += f"{9}{word[i]}" * a
            if b:
                s += f"{b}{word[i]}"
            i = j
        return s


# @lc code=end

if __name__ == "__main__":
    word: str = deserialize("str", read_line())
    ans = Solution().compressedString(word)
    print("\noutput:", serialize(ans, "string"))
