# Created by Jones at 2024/06/22 20:44
# leetgo: 1.4.7
# https://leetcode.cn/problems/lexicographically-smallest-beautiful-string/

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
    def smallestBeautifulString(self, s: str, k: int) -> str:
        k -= 1
        s = list(s)
        n = len(s)
        i = n - 1
        # try increase s[i]
        while i >= 0:
            idx = ord(s[i]) - ord("a")
            for ch in ascii_lowercase[idx + 1 : k + 1]:
                if (i == 0 or ch != s[i - 1]) and (i < 2 or ch != s[i - 2]):
                    s[i] = ch
                    # handle s[i+1:]
                    i += 1
                    while i < n:
                        for ch in ascii_lowercase[:k]:
                            if ch != s[i - 1] and (i < 2 or ch != s[i - 2]):
                                s[i] = ch
                                break
                        i += 1

                    return "".join(s)
            i -= 1

        return ""


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().smallestBeautifulString(s, k)
    print("\noutput:", serialize(ans, "string"))
