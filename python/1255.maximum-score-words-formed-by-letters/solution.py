# Created by Jones at 2024/05/24 10:33
# leetgo: 1.4.7
# https://leetcode.com/problems/maximum-score-words-formed-by-letters/

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
    def maxScoreWords(
        self, words: List[str], letters: List[str], score: List[int]
    ) -> int:
        """
        - `1 <= words.length <= 14`
        - `1 <= words[i].length <= 15`
        - `1 <= letters.length <= 100`
        - `letters[i].length == 1`
        - `score.length == 26`
        - `0 <= score[i] <= 10`
        - `words[i]`, `letters[i]` contains only lower case English letters.
        """

        def f(s):
            return Counter(ord(ch) - ord("a") for ch in s)

        nums = [f(s) for s in words]
        cnt = f(letters)
        res = 0
        n = len(words)
        for mask in range(1 << n):
            cur = Counter()
            for i in range(n):
                if mask >> i & 1:
                    cur += nums[i]
            if cur <= cnt:
                cur_res = sum(v * score[k] for k, v in cur.items())
                if cur_res > res:
                    res = cur_res
        return res


# @lc code=end

if __name__ == "__main__":
    words: List[str] = deserialize("List[str]", read_line())
    letters: List[str] = deserialize("List[str]", read_line())
    score: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxScoreWords(words, letters, score)
    print("\noutput:", serialize(ans, "integer"))
