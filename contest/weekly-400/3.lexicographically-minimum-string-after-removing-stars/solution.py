# Created by Jones at 2024/06/02 13:46
# leetgo: 1.4.7
# https://leetcode.cn/problems/lexicographically-minimum-string-after-removing-stars/
# https://leetcode.cn/contest/weekly-contest-400/problems/lexicographically-minimum-string-after-removing-stars/

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
    def clearStars(self, s: str) -> str:
        mp = defaultdict(list)
        for i, ch in enumerate(s):
            if ch == "*":
                mn = min(mp)
                mp[mn].pop()
                if len(mp[mn]) == 0:
                    del mp[mn]
            else:
                mp[ch].append(i)

        s = ["#"] * len(s)
        for ch, v in mp.items():
            for idx in v:
                s[idx] = ch

        return "".join(ch for ch in s if ch != "#")


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().clearStars(s)
    print("\noutput:", serialize(ans, "string"))
