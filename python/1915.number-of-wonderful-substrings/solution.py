# Created by Jones at 2024/04/30 12:44
# leetgo: 1.4.5
# https://leetcode.com/problems/number-of-wonderful-substrings/

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
    def wonderfulSubstrings(self, word: str) -> int:
        # we can use xor to show odd or even
        mp = {ch: ord(ch) - ord("a") for ch in ascii_lowercase[:10]}
        cnt = Counter()
        cnt[0] = 1

        res = 0
        x = 0
        for ch in word:
            x ^= 1 << mp[ch]
            res += cnt[x]  # the same
            cnt[x] += 1
        # print(cnt)
        # assume p is the prefix xor of word
        # if (p[x] ^ p[y]).bit_count() <= 1:
        # then is valid

        res2 = 0
        for x, cnt1 in cnt.items():
            for y, cnt2 in cnt.items():
                if x == y:  # we have compute the same
                    continue
                if (x ^ y).bit_count() <= 1:
                    res2 += cnt1 * cnt2
        return res + res2 // 2


# @lc code=end

if __name__ == "__main__":
    word: str = deserialize("str", read_line())
    ans = Solution().wonderfulSubstrings(word)
    print("\noutput:", serialize(ans, "long"))
