# Created by Jones at 2023/10/17 11:25
# leetgo: dev
# https://leetcode.cn/problems/sum-multiples/

from typing import *
from leetgo_py import *

import sys

sys.path.append("..")
from _LEETCODE import *

# @lc code=begin
# from sortedcontainers import SortedList


class Solution:
    def sumOfMultiples(self, n: int) -> int:
        return sum(x for x in range(1, n + 1) if x % 3 == 0 or x % 5 == 0 or x % 7 == 0)


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().sumOfMultiples(n)

    print("\noutput:", serialize(ans))
