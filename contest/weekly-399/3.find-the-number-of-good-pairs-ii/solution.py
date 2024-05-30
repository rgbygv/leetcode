# Created by Jones at 2024/05/30 19:14
# leetgo: 1.4.7
# https://leetcode.cn/problems/find-the-number-of-good-pairs-ii/
# https://leetcode.cn/contest/weekly-contest-399/problems/find-the-number-of-good-pairs-ii/

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
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        """
        - `1 <= n, m <= 10⁵`
        - `1 <= nums1[i], nums2[j] <= 10⁶`
        - `1 <= k <= 10³`
        """
        cnt = Counter()
        total = 0
        mx = 0
        for x in nums1:
            if x % k == 0:
                total += 1
                cnt[x // k] += 1
                mx = max(mx, x // k)
        res = 0
        for k, v in Counter(nums2).items():
            if k == 1:
                res += v * total
                continue
            for y in range(k, mx + 1, k):
                res += cnt[y] * v
                # ic(res, y, cnt)
        return res


# @lc code=end

if __name__ == "__main__":
    nums1: List[int] = deserialize("List[int]", read_line())
    nums2: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().numberOfPairs(nums1, nums2, k)
    print("\noutput:", serialize(ans, "long"))
