# Created by Jones at 2024/05/05 14:05
# leetgo: 1.4.6
# https://leetcode.cn/problems/defuse-the-bomb/

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
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0:
            return [0] * n
        code += code
        if k > 0:
            return [sum(code[i + 1 : i + k + 1]) for i in range(n)]
        return [sum(code[i + k : i]) for i in range(n, 2 * n)]


# @lc code=end

if __name__ == "__main__":
    code: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().decrypt(code, k)
    print("\noutput:", serialize(ans, "integer[]"))
