# Created by Jones at 2024/05/08 13:51
# leetgo: 1.4.6
# https://leetcode.com/problems/relative-ranks/

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
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        """
        Input: score = [5,4,3,2,1]
        Output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
        Explanation: The placements are [1ˢᵗ, 2ⁿᵈ, 3ʳᵈ, 4ᵗʰ, 5ᵗʰ].
        """
        q = sorted(zip(score, range(len(score))), reverse=True)
        for rank, (_, i) in enumerate(q, 1):
            if rank <= 3:
                if rank == 1:
                    score[i] = "Gold Medal"
                elif rank == 2:
                    score[i] = "Silver Medal"
                elif rank == 3:
                    score[i] = "Bronze Medal"
                else:
                    raise NotImplementedError
            else:
                score[i] = str(rank)
        return score


# @lc code=end

if __name__ == "__main__":
    score: List[int] = deserialize("List[int]", read_line())
    ans = Solution().findRelativeRanks(score)
    print("\noutput:", serialize(ans, "string[]"))
