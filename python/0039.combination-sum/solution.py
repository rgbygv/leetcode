# Created by Jones at 2024/04/20 13:56
# leetgo: 1.4.5
# https://leetcode.cn/problems/combination-sum/

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


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # since target <= 40, we can enumerate the number of candidate
        candidates.sort()
        while candidates and candidates[-1] > target:
            candidates.pop()
        res = []

        n = len(candidates)

        def dfs(i: int, target: int, path: list[int]):
            """use a[..=i] to combine target"""
            if target == 0:
                res.append(path[:])  # since path is mutable
                return
            if i == n or target < 0:
                return

            for times in count(0):
                if (next_target := target - times * candidates[i]) >= 0:
                    dfs(i + 1, next_target, path + [candidates[i]] * times)
                else:
                    break

        path = []
        dfs(0, target, path)

        return res


# @lc code=end

if __name__ == "__main__":
    candidates: List[int] = deserialize("List[int]", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().combinationSum(candidates, target)
    print("\noutput:", serialize(ans, "integer[][]"))
