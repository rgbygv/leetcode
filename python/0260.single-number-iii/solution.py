# Created by Jones at 2023/10/16 14:41
# leetgo: dev
# https://leetcode.cn/problems/single-number-iii/

from typing import *
from leetgo_py import *

import sys 
sys.path.append("..") 
from _LEETCODE import *

# @lc code=begin
# from sortedcontainers import SortedList

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        x = reduce(xor, nums)
        
        lowbit = x & -x
        
        x,y = 0, 0
        for num in nums:
            if num & lowbit != 0:
                x ^= num
            else:
                y ^= num
        return [x, y]


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().singleNumber(nums)

    print("\noutput:", serialize(ans))
