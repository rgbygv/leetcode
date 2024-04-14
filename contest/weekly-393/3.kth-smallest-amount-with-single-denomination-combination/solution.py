# Created by Jones at 2024/04/14 20:40
# leetgo: 1.4.5
# https://leetcode.cn/problems/kth-smallest-amount-with-single-denomination-combination/
# https://leetcode.cn/contest/weekly-contest-393/problems/kth-smallest-amount-with-single-denomination-combination/

from typing import *
from leetgo_py import *

from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from copy import deepcopy
from functools import cache, cmp_to_key, lru_cache, reduce
from heapq import heapify, heappop, heappush, heappushpop, heapreplace
from itertools import accumulate, chain, count, pairwise, zip_longest
from math import ceil, comb, floor, gcd, inf, isqrt, log2, perm, sqrt, lcm
from operator import xor
from pprint import pprint
from string import ascii_lowercase
from typing import List, Optional

# @lc code=begin


class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        if 1 in coins:
            return k
        coins.sort()
        a = []
        for x in coins:
            ok = True
            for y in a:
                # x can be obtained from y
                if x % y == 0:
                    ok = False
                    break
            if ok:
                a.append(x)
        # 2 3 5 7 11 13 17 19 23
        coins = a
        mp = []

        n = len(coins)
        for mask in range(1, 1 << n):
            x = 1
            for i in range(n):
                if mask >> i & 1:
                    x = lcm(x, coins[i])
            op = (mask.bit_count() & 1) * 2 - 1
            mp.append((x, op))

        l = coins[0]
        r = coins[0] * k
        while l < r:
            mid = (l + r) >> 1

            def check(mid):
                # how to handle `a number is count multi times`
                # combine math
                res = 0
                for x, op in mp:
                    cnt = mid // x
                    res += cnt * op
                return res >= k

            # print(mid, check(mid))
            if check(mid):
                r = mid
            else:
                l = mid + 1
        return l


# @lc code=end

if __name__ == "__main__":
    coins: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().findKthSmallest(coins, k)
    print("\noutput:", serialize(ans, "long"))
