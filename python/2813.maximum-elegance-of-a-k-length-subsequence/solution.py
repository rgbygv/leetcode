# Created by Jones at 2024/06/13 14:12
# leetgo: 1.4.7
# https://leetcode.cn/problems/maximum-elegance-of-a-k-length-subsequence/

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
    def findMaximumElegance(self, items: List[List[int]], k: int) -> int:
        """
        - `1 <= items.length == n <= 10⁵`
        - `items[i].length == 2`
        - `items[i][0] == profitᵢ`
        - `items[i][1] == categoryᵢ`
        - `1 <= profitᵢ <= 10⁹`
        - `1 <= categoryᵢ <= n `
        - `1 <= k <= n`
        """

        """
        sum(profit) + len(set(type)) ** 2
        """
        items.sort(reverse=True)

        res = 0
        s = 0

        category = set()
        dup = []

        for i in range(k):
            p, t = items[i]
            if t in category:
                dup.append(p)
            else:
                category.add(t)
            s += p

        res = s + len(category) ** 2

        for i in range(k, len(items)):
            p, t = items[i]
            if t not in category and dup:
                # try decrease profit, add category
                category.add(t)
                s += p - dup.pop()
            res = max(res, s + len(category) ** 2)

        return res


# @lc code=end

if __name__ == "__main__":
    items: List[List[int]] = deserialize("List[List[int]]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().findMaximumElegance(items, k)
    print("\noutput:", serialize(ans, "long"))
