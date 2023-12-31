# Created by Bob at 2023/12/31 15:57
# leetgo: dev
# https://leetcode.cn/problems/palindrome-rearrangement-queries/
# https://leetcode.cn/contest/weekly-contest-378/problems/palindrome-rearrangement-queries/

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


class Solution:
    def canMakePalindromeQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        m = len(s)
        n = m >> 1

        s1, s2 = s[:n], s[n:][::-1]

        if Counter(s1) != Counter(s2):
            return [False] * len(queries)
        left = [0] * (n + 1)
        for i in range(n):
            if s1[i] == s2[i]:
                left[i] += 1 + left[i - 1]

        # right = [0] * (n + 1)
        # for i in range(n - 1, -1, -1):
        #     if s1[i] == s2[i]:
        #         right[i] += 1 + right[i + 1]

        def check(l, r):
            if l > r:
                return True
            return left[r] - left[l - 1] == r - l + 1

        mp1 = defaultdict(list)
        for i, ch in enumerate(s1):
            mp1[ch].append(i)
        mp2 = defaultdict(list)
        for i, ch in enumerate(s2):
            mp2[ch].append(i)

        def check2(a, b, c, d):
            for ch in ascii_lowercase:
                v1 = mp1[ch]
                v2 = mp2[ch]

                def size(v, l: int, r: int):
                    return bisect_right(v, r) - bisect_left(v, l)

                if a > c:
                    a, b, c, d = c, d, a, b
                    v1, v2 = v2, v1

                # s1(a,b) >= s2(a,c-1)
                if not size(v1, a, b) >= size(v2, a, c - 1):
                    return False
                # s2(c,d) >= s1(b+1,d)
                if not size(v2, c, d) >= size(v1, b + 1, d):
                    return False
            return True

        res = []
        for a, b, c, d in queries:
            c, d = m - 1 - d, m - 1 - c

            print((a, b), (c, d), s1, s2)
            if a > d:
                cur = check(0, c - 1) and check(d + 1, a - 1) and check(b + 1, n - 1)
            elif b < c:
                cur = check(0, a - 1) and check(b + 1, c - 1) and check(d + 1, n - 1)
            else:
                if (a, b) == (0, n - 1) or (c, d) == (0, n - 1):
                    cur = True
                else:
                    q = sorted([a, b, c, d])
                    # a, c, b, d = q
                    # s1 a....b...
                    # s2 ....c...d
                    # s1(a,b) >= s2(a,c-1) and s2(c,d) >= s1(b+1,d)
                    cur = (
                        check(0, q[0] - 1)
                        and check(q[-1] + 1, n - 1)
                        and check2(a, b, c, d)
                    )
            res.append(cur)
        return res


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    queries: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().canMakePalindromeQueries(s, queries)

    print("\noutput:", serialize(ans))
