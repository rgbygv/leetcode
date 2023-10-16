# Created by Jones at 2023/10/16 14:53
# leetgo: dev
# https://leetcode.cn/problems/pascals-triangle-ii/

from typing import *
from leetgo_py import *

import sys 
sys.path.append("..") 
from _LEETCODE import *

# @lc code=begin
# from sortedcontainers import SortedList

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pre = [1]
        for i in range(1,rowIndex+1):
            cur = [1] * (i+1)
            for j in range(1, i):
                cur[j] = pre[j] + pre[j-1]
            pre = cur
        return pre

# @lc code=end

if __name__ == "__main__":
    rowIndex: int = deserialize("int", read_line())
    ans = Solution().getRow(rowIndex)

    print("\noutput:", serialize(ans))
