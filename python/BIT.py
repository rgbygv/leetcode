class BIT:
    def __init__(self, n: int) -> None:
        self.q = [0] * (n + 1)

    def lowbit(self, x: int):
        return x & -x

    def update(self, x: int, d: int):
        while x < len(self.q):
            self.q[x] += d
            x += self.lowbit(x)

    def query(self, x: int) -> int:
        res = 0
        while x > 0:
            res += self.q[x]
            x -= self.lowbit(x)
        return res


# class BIT:
#     def __init__(self, n: int) -> None:
#         self.n = n + 1
#         self.q = {}

#     def lowbit(self, x: int):
#         return x & -x

#     def update(self, x: int, val: int):
#         while x < self.n:
#             if x not in self.q or val < self.q[x]:
#                 self.q[x] = val
#             x += self.lowbit(x)

#     def query(self, x: int) -> int:
#         res = 10**18
#         while x > 0:
#             if x in self.q and self.q[x] < res:
#                 res = self.q[x]
#             x -= self.lowbit(x)
#         return res
