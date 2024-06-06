# Created by Jones at 2024/06/06 08:36
# leetgo: 1.4.7
# https://leetcode.com/problems/hand-of-straights/

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
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0:
            return False
        # find min, and check(min,min+size-1)
        cnt = Counter(hand)
        heapify(hand)
        for _ in range(n // groupSize):
            while hand:
                mn = heappop(hand)
                if cnt[mn] > 0:
                    break
            for i in range(groupSize):
                x = mn + i
                cnt[x] -= 1
                if cnt[x] < 0:
                    return False
        return True


# @lc code=end

if __name__ == "__main__":
    hand: List[int] = deserialize("List[int]", read_line())
    groupSize: int = deserialize("int", read_line())
    ans = Solution().isNStraightHand(hand, groupSize)
    print("\noutput:", serialize(ans, "boolean"))
