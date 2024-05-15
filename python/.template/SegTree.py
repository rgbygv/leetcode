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


# class SegTree:
#     def __init__(self, nums) -> None:
#         self.n = n = len(nums)
#         N = n * 4
#         self.nums = nums
#         self.q = [0] * N
#         self.lazy = [True] * N
#         # root start from 0
#         self.build(0, 0, n - 1)

#     def calculate(self, o: int, l: int, r: int):
#         self.q[o] = self.q[l] + self.q[r]

#     def build(self, o: int, l: int, r: int):
#         if l == r:
#             self.q[o] = self.nums[l]
#             return
#         mid = (l + r) >> 1
#         left, right = o * 2 + 1, o * 2 + 2
#         self.build(left, l, mid)
#         self.build(right, mid + 1, r)
#         self.calculate(o, left, right)

#     def update(self, o: int, l: int, r: int, L: int, R: int):
#         if L == l and r == R:
#             self.lazy[o] = not self.lazy[o]
#             ones = self.q[o]
#             zeros = R - L + 1 - ones
#             self.q[o] = zeros
#             return

#         left, right = o * 2 + 1, o * 2 + 2
#         mid = (l + r) >> 1

#         if not self.lazy[o]:
#             self.update(left, l, mid, l, mid)
#             self.update(right, mid + 1, r, mid + 1, r)
#             self.lazy[o] = True

#         if R <= mid:
#             self.update(left, l, mid, L, R)
#         elif L > mid:
#             self.update(right, mid + 1, r, L, R)
#         else:
#             self.update(left, l, mid, L, mid)
#             self.update(right, mid + 1, r, mid + 1, R)

#         self.calculate(o, left, right)

#     def query(self, o: int, l: int, r: int, L: int, R: int):
#         if L == l and r == R:
#             return self.q[o]

#         left, right = o * 2 + 1, o * 2 + 2
#         mid = (l + r) >> 1

#         if not self.lazy[o]:
#             self.update(left, l, mid, l, mid)
#             self.update(right, mid + 1, r, mid + 1, r)
#             self.lazy[o] = True
#         res = 0
#         if R <= mid:
#             res += self.query(left, l, mid, L, R)
#         elif L > mid:
#             res += self.query(right, mid + 1, r, L, R)
#         else:
#             res += self.query(left, l, mid, L, mid)
#             res += self.query(right, mid + 1, r, mid + 1, R)

#         return res
