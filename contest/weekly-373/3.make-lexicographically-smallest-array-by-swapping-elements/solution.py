# Created by Jones at 2023/11/26 10:30
# leetgo: dev
# https://leetcode.cn/problems/make-lexicographically-smallest-array-by-swapping-elements/
# https://leetcode.cn/contest/weekly-contest-373/problems/make-lexicographically-smallest-array-by-swapping-elements/

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
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        mp = defaultdict(list)
        for i, x in enumerate(nums):
            mp[x].append(i)

        res = [0] * len(nums)
        q = sorted(mp)
        i = 0
        while i < len(q):
            j = i + 1
            idxs = mp[q[i]]
            vals = [q[i]] * len(mp[q[i]])
            while j < len(q) and q[j] - q[j - 1] <= limit:
                idxs.extend(mp[q[j]])
                vals.extend([q[j]] * len(mp[q[j]]))
                j += 1
            idxs.sort()
            for idx, val in zip(idxs, vals):
                res[idx] = val
            i = j

        return res


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    limit: int = deserialize("int", read_line())
    ans = Solution().lexicographicallySmallestArray(nums, limit)

    print("\noutput:", serialize(ans))
