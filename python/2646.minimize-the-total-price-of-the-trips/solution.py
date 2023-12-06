# Created by Jones at 2023/12/06 13:56
# leetgo: dev
# https://leetcode.cn/problems/minimize-the-total-price-of-the-trips/

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
from string import ascii_lowercase
from typing import List, Optional

# @lc code=begin
# from sortedcontainers import SortedList


class Solution:
    def minimumTotalPrice(
        self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]
    ) -> int:
        """
        #
        f(x,y) = f(x) + f(y) - 2 * lca(x,y)
        # in
        f(x,y) = f(x) - f(p[y])
        """

        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        d = [0] * n
        p = [-1] * n

        def depth(x, fa, h):
            d[x] = h
            p[x] = fa
            for y in g[x]:
                if y == fa:
                    continue
                depth(y, x, h + 1)

        depth(0, -1, 0)
        # print(d)
        # print(p)

        def lca(x, y):
            # print(x,y)
            if d[x] == d[y]:
                if x == y:
                    cnt[x] += 1
                    return x
                cnt[x] += 1
                cnt[y] += 1
                return lca(p[x], p[y])
            # if d[x] < d[y]:
            #     return lca(x, p[y])
            cnt[x] += 1
            return lca(p[x], y)

        cnt = [0] * (n + 1)  # -1 for dummy
        for x, y in trips:
            if d[x] < d[y]:
                x, y = y, x
            lca(x, y)
            # tmp = lca(x, y)
            # print(x, y, tmp)
            # if tmp == y:
            #     cnt[x] += 1
            #     cnt[p[y]] -= 1
            # else:
            #     cnt[x] += 1
            #     cnt[y] += 1
            #     cnt[tmp] -= 2
        # print(cnt)
        # a = [w * pr for w, pr in zip(cnt, price)]
        # print(a)

        @cache
        def dfs(x: int, fa: int, changed: bool):
            # don't half
            op2 = (price[x]) * cnt[x]
            for y in g[x]:
                if y == fa:
                    continue
                op2 += dfs(y, x, False)
            if changed:
                return op2

            op1 = (price[x] // 2) * cnt[x]
            for y in g[x]:
                if y == fa:
                    continue
                op1 += dfs(y, x, True)
            return min(op1, op2)

        return dfs(0, -1, False)


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    price: List[int] = deserialize("List[int]", read_line())
    trips: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().minimumTotalPrice(n, edges, price, trips)

    print("\noutput:", serialize(ans))
