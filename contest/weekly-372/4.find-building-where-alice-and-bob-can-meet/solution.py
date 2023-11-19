# Created by Jones at 2023/11/19 10:30
# leetgo: dev
# https://leetcode.cn/problems/find-building-where-alice-and-bob-can-meet/
# https://leetcode.cn/contest/weekly-contest-372/problems/find-building-where-alice-and-bob-can-meet/

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
class SegmentTree:
    def __init__(self, nums):
        n = len(nums)
        # f记录的是特定区间，f[k]，序号为k的点：该节点掌管的索引为l,r，值区间l~r的数字总和
        self.nums = [0] + nums  # 加一个哨兵节点，使得数组的有效索引为1～n
        self.f = [0 for _ in range(4 * n)]
        self.buildTree(1, 1, n)

    def buildTree(self, k, l, r):
        # 序号为k的索引，掌管的范围是l~r
        # 这里要注意，对于一棵数组长度确定的线段树，k是可以唯一确定l,r的
        # 例如根节点1 一定对应 1~n
        # 即同一个k对应唯一的l,r
        if l == r:
            # 叶子节点
            self.f[k] = self.nums[l]
            return
        mid = (l + r) // 2
        # 分治 + 后序遍历的思想
        self.buildTree(2 * k, l, mid)  # 处理左孩子
        self.buildTree(2 * k + 1, mid + 1, r)  # 处理右孩子
        self.f[k] = max(self.f[2 * k], self.f[2 * k + 1])  # 父节点的信息为左右孩子汇总

    def update(self, k, l, r, i, x):
        # 序号为k的索引，掌管的范围是l~r
        # 对数组索引为i的节点增量更新x
        self.f[k] += x
        if l == r:
            # 叶子节点
            return
        mid = (l + r) // 2
        # 看索引i在左右子树的哪一边。递归更新
        if i <= mid:  # 在左子树
            self.update(2 * k, l, mid, i, x)
        elif i > mid:  # 在右子树
            self.update(2 * k + 1, mid + 1, r, i, x)

    @cache
    def query(self, k, l, r, start, end):
        # start~end始终是l~r的子区间
        # 序号为k的索引，掌管的范围是l~r
        # 在整棵树上进行搜寻 start~end 索引所汇总的范围和
        if l == start and r == end:
            return self.f[k]
        mid = (l + r) // 2
        if end <= mid:  # 如果start~end完全在左半边，则只需要算左子树
            return self.query(2 * k, l, mid, start, end)
        if mid < start:  # 如果start~end完全在右半边，则只需要算右子树
            return self.query(2 * k + 1, mid + 1, r, start, end)
        # 否则，需要同时考虑左右孩子
        leftPart = self.query(2 * k, l, mid, start, mid)  # 注意：在这里最后一个参数是mid而不是end
        rightPart = self.query(
            2 * k + 1, mid + 1, r, mid + 1, end
        )  # 注意：在这里倒数第二个参数是mid+1而不是start
        # 因为：# start~end始终是l~r的子区间，否则递归会没有出口
        return max(leftPart, rightPart)


class Solution:
    def leftmostBuildingQueries(
        self, heights: List[int], queries: List[List[int]]
    ) -> List[int]:
        n = len(heights)
        st = SegmentTree(heights)
        res = []

        for x, y in queries:
            if x > y:
                x, y = y, x
            if heights[y] > heights[x] or x == y:
                res.append(y)
                continue
            hx = max(heights[x], heights[y])
            l = y + 1
            r = n - 1
            while l < r:
                mid = (l + r) >> 1
                cur = st.query(1, 1, n, l + 1, mid + 1)
                # print(l, r, cur)
                if cur > hx:
                    r = mid
                else:
                    l = mid + 1
            if l >= n or heights[l] <= hx:
                res.append(-1)
            else:
                res.append(l)
        st.query.cache_clear()
        return res


# @lc code=end

if __name__ == "__main__":
    heights: List[int] = deserialize("List[int]", read_line())
    queries: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().leftmostBuildingQueries(heights, queries)

    print("\noutput:", serialize(ans))
