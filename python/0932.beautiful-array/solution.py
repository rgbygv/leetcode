# Created by Jones at 2024/05/01 15:29
# leetgo: 1.4.5
# https://leetcode.cn/problems/beautiful-array/

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
    def beautifulArray(self, n: int) -> List[int]:
        # if n <= 2:
        #     return list(range(1, n + 1))

        def construct(n: int):
            if n <= 2:
                return list(range(1, n + 1))
            left = construct((n + 1) // 2)
            for i, x in enumerate(left):
                left[i] = x * 2 - 1
            right = construct(n // 2)
            for i, x in enumerate(right):
                right[i] = x * 2
            return left + right

        return construct(n)

        """
        1 3 2
        1 3 2 4
        1 5 3 2 4

        group by odd and even 
        1 5 9 7 3  it's wrong
        

        if we add x

        then we should check each mid  x - 2, x - 4, x - 6 ...
        the y = 2 * mid - x

        we should let mid not between (x, y)
        (y x mid)  and  (x y mid) is valid
        

        let's construct some 

        """

        # def construct(x: int, l: int, r: int):
        #     if l > r:
        #         return
        #     res = [0] * (r - l + 1)
        #     while l <= r:
        #         res[l] = x
        #         x += 2
        #         l += 1
        #         if l <= r:
        #             res[r] = x
        #             x += 2
        #             r -= 1
        #     return res

        # return construct(1, 0, (n + 1) // 2 - 1) + construct(2, 0, n // 2 - 1)


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().beautifulArray(n)
    print("\noutput:", serialize(ans, "integer[]"))
