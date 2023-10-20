# Created by Jones at 2023/10/20 13:47
# leetgo: dev
# https://leetcode.cn/problems/flatten-nested-list-iterator/

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
from string import ascii_lowercase
from typing import List, Optional

# @lc code=begin
# from sortedcontainers import SortedList

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """



class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.st = self.dfs(nestedList)[::-1]

    
    def dfs(self, nestedList: [NestedInteger]):
        st = []
        for nested in nestedList:
            if nested.isInteger():
                st.append(nested.getInteger())
            else:
                st.extend(self.dfs(nested.getList()))
        return st

    
    def next(self) -> int:
        return self.st.pop()
        
    
    def hasNext(self) -> bool:
        return bool(self.st)
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

# @lc code=end

# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    nestedList: List[NestedInteger] = deserialize("List[NestedInteger]", read_line())
    ans = Solution().(nestedList)

    print("\noutput:", serialize(ans))
