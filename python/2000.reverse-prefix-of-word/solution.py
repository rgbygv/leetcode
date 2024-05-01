# Created by Jones at 2024/05/01 13:29
# leetgo: 1.4.5
# https://leetcode.com/problems/reverse-prefix-of-word/

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
    def reversePrefix(self, word: str, ch: str) -> str:
        i = word.find(ch)
        if i == -1:
            return word
        return word[: i + 1][::-1] + word[i + 1 :]


# @lc code=end

if __name__ == "__main__":
    word: str = deserialize("str", read_line())
    ch: str = deserialize("str", read_line())
    ans = Solution().reversePrefix(word, ch)
    print("\noutput:", serialize(ans, "string"))
