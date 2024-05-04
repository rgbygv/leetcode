# Created by Jones at 2024/05/04 14:44
# leetgo: 1.4.6
# https://leetcode.cn/problems/filling-bookcase-shelves/

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
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        # - `1 <= books.length <= 1000`
        # - `1 <= thicknessᵢ <= shelfWidth <= 1000`
        # - `1 <= heightᵢ <= 1000`
        n = len(books)

        f = [inf] * (n + 1)
        f[0] = 0
        for i, (width, height) in enumerate(books, 1):
            # put at a new level
            f[i] = f[i - 1] + height
            # put with before
            rest = shelfWidth - width
            max_height = height
            for j in range(i - 1, 0, -1):
                w, h = books[j - 1]
                rest -= w
                max_height = max(max_height, h)
                if rest < 0:
                    break
                f[i] = min(f[i], f[j - 1] + max_height)
        # ic(f)
        return f[-1]


# @lc code=end

if __name__ == "__main__":
    books: List[List[int]] = deserialize("List[List[int]]", read_line())
    shelfWidth: int = deserialize("int", read_line())
    ans = Solution().minHeightShelves(books, shelfWidth)
    print("\noutput:", serialize(ans, "integer"))
