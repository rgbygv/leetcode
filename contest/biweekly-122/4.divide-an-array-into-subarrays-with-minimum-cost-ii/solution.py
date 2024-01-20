# Created by Jones at 2024/01/20 22:30
# leetgo: dev
# https://leetcode.cn/problems/divide-an-array-into-subarrays-with-minimum-cost-ii/
# https://leetcode.cn/contest/biweekly-contest-122/problems/divide-an-array-into-subarrays-with-minimum-cost-ii/

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
from sortedcontainers import SortedList


class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        res = nums[0]
        n = len(nums)
        i = 2
        # select k-2 from a[i:i+dist]
        q = SortedList(nums[i : i + dist])
        s = sum(q[: k - 2])
        ans = nums[i - 1] + s
        while i + min(dist, k - 3) < n:
            # add nums[i+dist]
            if i + dist < n:
                x = nums[i + dist]
                if k - 3 >= 0 and x < q[k - 3]:
                    s -= q[k - 3] - x
                q.add(x)
            if len(q) <= k - 2:
                break
            x = nums[i]
            if k - 3 >= 0 and x <= q[k - 3]:
                s += q[k - 2] - x
            q.remove(x)
            cur = nums[i] + s
            ans = min(cur, ans)
            i += 1

        return res + ans


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    dist: int = deserialize("int", read_line())
    ans = Solution().minimumCost(nums, k, dist)

    print("\noutput:", serialize(ans))
