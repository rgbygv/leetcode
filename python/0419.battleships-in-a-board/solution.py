# Created by Jones at 2024/06/11 15:04
# leetgo: 1.4.7
# https://leetcode.cn/problems/battleships-in-a-board/

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
    def countBattleships(self, board: List[List[str]]) -> int:
        """
        - `m == board.length`
        - `n == board[i].length`
        - `1 <= m, n <= 200`
        - `board[i][j]` is either `'.'` or `'X'`.

        **Follow up:** Could you do it in one-pass, using only `O(1)` extra memory and without modifying the
        values `board`?
        """
        m, n = len(board), len(board[0])

        res = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == "X":
                    res += 1
                    for k in range(j + 1, n):
                        if board[i][k] == "X":
                            board[i][k] = "."
                        else:
                            break

                    for k in range(i + 1, m):
                        if board[k][j] == "X":
                            board[k][j] = "."
                        else:
                            break
                    board[i][j] = "."
        return res

        return res


# @lc code=end

if __name__ == "__main__":
    board: List[List[str]] = deserialize("List[List[str]]", read_line())
    ans = Solution().countBattleships(board)
    print("\noutput:", serialize(ans, "integer"))
