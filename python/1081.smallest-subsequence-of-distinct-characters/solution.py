# Created by Jones at 2024/05/03 14:40
# leetgo: 1.4.5
# https://leetcode.cn/problems/smallest-subsequence-of-distinct-characters/

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
    def smallestSubsequence(self, s: str) -> str:
        cnt = Counter(s)

        st = []
        seen = set()
        for ch in s:
            if ch not in seen:
                while st and ch < st[-1] and cnt[st[-1]] > 0:
                    seen.remove(st.pop())
                seen.add(ch)
                st.append(ch)
            cnt[ch] -= 1
        return "".join(st)


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().smallestSubsequence(s)
    print("\noutput:", serialize(ans, "string"))
