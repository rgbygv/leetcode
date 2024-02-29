# Created by Jones at 2024/02/29 14:26
# leetgo: 1.4.1
# https://leetcode.cn/problems/count-number-of-possible-root-nodes/

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
    def rootCount(
        self, edges: List[List[int]], guesses: List[List[int]], k: int
    ) -> int:
        n = len(edges) + 1
        g = [[] for _ in range(n)]

        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        guesses = set(tuple(e) for e in guesses)

        # assume x as root
        def dfs(x: int, fa: int):
            res = 0
            for y in g[x]:
                if y == fa:
                    continue
                res += (x, y) in guesses
                res += dfs(y, x)
            return res

        cnt = dfs(0, -1)
        res = cnt >= k

        def change_root(x: int, fa: int, cnt: int):
            nonlocal res
            for y in g[x]:
                if y == fa:
                    continue
                # change root from x to y
                cur = cnt
                cur += int((y, x) in guesses) - int((x, y) in guesses)
                if cur >= k:
                    res += 1
                change_root(y, x, cur)

        change_root(0, -1, cnt)
        return int(res)


# @lc code=end

if __name__ == "__main__":
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    guesses: List[List[int]] = deserialize("List[List[int]]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().rootCount(edges, guesses, k)
    print("\noutput:", serialize(ans, "integer"))
