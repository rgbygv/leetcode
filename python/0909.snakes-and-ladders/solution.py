# Created by Jones at 2024/04/30 15:15
# leetgo: 1.4.5
# https://leetcode.cn/problems/snakes-and-ladders/

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
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        # - `n == board.length == board[i].length`
        # - `2 <= n <= 20`
        # - `board[i][j]` is either `-1` or in the range `[1, n²]`.
        # - The squares labeled `1` and `n²` do not have any ladders or snakes

        n = len(board)
        end = n * n
        # bfs

        def trans(curr: int):
            a, b = divmod(curr - 1, n)
            return (n - 1 - a, b) if a & 1 == 0 else (n - 1 - a, n - 1 - b)

        f = [False] * (end + 1)
        q = [1]
        f[1] = True
        t = 0

        while q:
            # print(t, q)
            p = []
            for curr in q:
                if curr == end:
                    return t
                for next in range(curr + 1, min(curr + 6, end) + 1):
                    x, y = trans(next)
                    if board[x][y] != -1:
                        next = board[x][y]
                    # print(x, y, next)
                    if not f[next]:
                        f[next] = True
                        p.append(next)
            q = p
            t += 1
        return -1


# @lc code=end

if __name__ == "__main__":
    board: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().snakesAndLadders(board)
    print("\noutput:", serialize(ans, "integer"))
