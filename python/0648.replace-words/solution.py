# Created by Jones at 2024/06/07 12:37
# leetgo: 1.4.7
# https://leetcode.com/problems/replace-words/

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
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        """
        - `1 <= dictionary.length <= 1000`
        - `1 <= dictionary[i].length <= 100`
        - `dictionary[i]` consists of only lower-case letters.
        - `1 <= sentence.length <= 10⁶`
        - `sentence` consists of only lower-case letters and spaces.
        - The number of words in `sentence` is in the range `[1, 1000]`
        - The length of each word in `sentence` is in the range `[1, 1000]`
        - Every two consecutive words in `sentence` will be separated by exactly one space.
        - `sentence` does not have leading or trailing spaces.
        """
        res = []
        can = set(dictionary)
        for word in sentence.split():
            s = ""
            for ch in word:
                s += ch
                if s in can:
                    res.append(s)
                    s = ""
                    break
            if s:
                res.append(s)
        return " ".join(res)


# @lc code=end

if __name__ == "__main__":
    dictionary: List[str] = deserialize("List[str]", read_line())
    sentence: str = deserialize("str", read_line())
    ans = Solution().replaceWords(dictionary, sentence)
    print("\noutput:", serialize(ans, "string"))
