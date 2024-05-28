# Created by Jones at 2024/05/28 15:33
# leetgo: 1.4.7
# https://leetcode.cn/problems/minimum-adjacent-swaps-to-reach-the-kth-smallest-number/

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
    def getMinSwaps(self, num: str, k: int) -> int:
        """
        "5489355142"
        """
        s = list(num)
        n = len(s)
        for _ in range(k):
            cnt = [0] * 10
            for i in range(n - 1, -1, -1):
                x = int(s[i])
                ok = False
                for y in range(x + 1, 10):
                    if cnt[y]:
                        ok = True
                        cnt[y] -= 1
                        s[i] = str(y)
                        q = [str(x)]
                        for y, size in enumerate(cnt):
                            if size:
                                q.extend([str(y)] * size)
                        s[i + 1 :] = sorted(q)
                        break

                cnt[x] += 1
                if ok:
                    break

        i = 0
        res = 0
        while i < n:
            if num[i] != s[i]:
                for j in range(i + 1, n):
                    if s[j] == num[i]:
                        res += j - i
                        for k in range(j, i, -1):
                            s[k], s[k - 1] = s[k - 1], s[k]
                        break

            i += 1
        return res


# @lc code=end

if __name__ == "__main__":
    num: str = deserialize("str", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().getMinSwaps(num, k)
    print("\noutput:", serialize(ans, "integer"))
