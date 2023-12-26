# Created by Bob at 2023/12/26 21:20
# leetgo: dev
# https://leetcode.cn/problems/maximum-students-taking-exam/

from typing import *
from leetgo_py import *

from functools import cache
# @lc code=begin


class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        m = len(seats)
        n = len(seats[0])

        def check(last_row, cur_row, i: int):
            return not (
                (i > 0 and last_row >> (i - 1) & 1)
                or (i < n and last_row >> (i + 1) & 1)
                or (i > 0 and cur_row >> (i - 1) & 1)
            )

        @cache
        def dfs(i: int, j: int, last_row: int, cur_row: int):
            if i == m:
                return 0

            # jump to the next line
            if j == n:
                return dfs(i + 1, 0, cur_row, 0)

            row = seats[i]
            # don't select
            res = dfs(i, j + 1, last_row, cur_row)
            # select a seat
            if row[j] == "." and check(last_row, cur_row, j):
                res = max(res, 1 + dfs(i, j + 1, last_row, cur_row | (1 << j)))

            return res

        return dfs(0, 0, 0, 0)


# @lc code=end

if __name__ == "__main__":
    seats: List[List[str]] = deserialize("List[List[str]]", read_line())
    ans = Solution().maxStudents(seats)

    print("\noutput:", serialize(ans))
