# Created by Jones at 2024/05/25 13:29
# leetgo: 1.4.7
# https://leetcode.com/problems/word-break-ii/

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
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        """
        - `1 <= s.length <= 20`
        - `1 <= wordDict.length <= 1000`
        - `1 <= wordDict[i].length <= 10`
        - `s` and `wordDict[i]` consist of only lowercase English letters.
        - All the strings of `wordDict` are **unique**.
        - Input is generated in a way that the length of the answer doesn't exceed 10.
        """
        res = []
        can = set(wordDict)
        path = []
        n = len(s)

        def dfs(i: int):
            if i == n:
                res.append(" ".join(path[:]))
                return True
            for j in range(i + 1, n + 1):
                cur = s[i:j]
                if cur in can:
                    path.append(cur)
                    dfs(j)
                    path.pop()

        dfs(0)
        return res


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    wordDict: List[str] = deserialize("List[str]", read_line())
    ans = Solution().wordBreak(s, wordDict)
    print("\noutput:", serialize(ans, "string[]"))
