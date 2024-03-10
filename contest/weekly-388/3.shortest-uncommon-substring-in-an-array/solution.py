# Created by Jones at 2024/03/10 13:54
# leetgo: 1.4.1
# https://leetcode.cn/problems/shortest-uncommon-substring-in-an-array/
# https://leetcode.cn/contest/weekly-contest-388/problems/shortest-uncommon-substring-in-an-array/

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
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        res = []

        seen = defaultdict(int)
        for s in arr:
            n = len(s)
            for i in range(n):
                for j in range(i + 1, n + 1):
                    seen[s[i:j]] += 1

        for s in arr:
            n = len(s)
            for i in range(n):
                for j in range(i + 1, n + 1):
                    seen[s[i:j]] -= 1
            ok = False
            for size in range(1, n + 1):
                ans = None
                for i in range(size, n + 1):
                    tmp = s[i - size : i]
                    if seen[tmp] == 0:
                        if not ans or tmp < ans:
                            ans = tmp
                if ans:
                    res.append(ans)
                    ok = True
                    break
            if not ok:
                res.append("")
            for i in range(n):
                for j in range(i + 1, n + 1):
                    seen[s[i:j]] += 1
        return res


# @lc code=end

if __name__ == "__main__":
    arr: List[str] = deserialize("List[str]", read_line())
    ans = Solution().shortestSubstrings(arr)
    print("\noutput:", serialize(ans, "string[]"))
