# Created by Jones at 2024/04/26 22:43
# leetgo: 1.4.5
# https://leetcode.cn/problems/number-of-atoms/

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
    def countOfAtoms(self, formula: str) -> str:
        n = len(formula)
        i = 0
        st = []

        def handle_num():
            nonlocal i
            num = 0
            while i < n and formula[i].isdigit():
                num = num * 10 + int(formula[i])
                i += 1
            return num

        def handle_bracket(num: int = 1):
            st.pop()  # remove ')'
            tmp = []
            while st[-1] != "(":
                (ch, c) = st.pop()
                tmp.append((ch, c * num))
            st.pop()  # remove '('
            st.extend(tmp[::-1])  # add back elements inside '()

        while i < n:
            # print(st)
            if formula[i] in "()":
                st.append(formula[i])
                if formula[i] == ")" and (i + 1 == n or not formula[i + 1].isdigit()):
                    handle_bracket()
                i += 1
            elif formula[i].isdigit():
                num = handle_num()
                if st[-1] == ")":
                    handle_bracket(num)
                else:
                    ch, c = st.pop()
                    st.append((ch, c * num))

            else:  # alpha
                # handle situation like `(H)`, don't have num after ')', it may consume much time
                # maybe better way it's remove the useless ()
                element = ""
                while i < n and formula[i].isalpha():
                    if formula[i].isupper() and element != "":  # a new element
                        st.append((element, 1))
                        element = ""
                    element += formula[i]
                    i += 1
                st.append((element, 1))

        cnt = Counter()
        for element, c in st:
            cnt[element] += c

        res = ""
        for element in sorted(cnt):
            res += element
            if cnt[element] > 1:
                res += str(cnt[element])
        return res


# @lc code=end

if __name__ == "__main__":
    formula: str = deserialize("str", read_line())
    ans = Solution().countOfAtoms(formula)
    print("\noutput:", serialize(ans, "string"))
