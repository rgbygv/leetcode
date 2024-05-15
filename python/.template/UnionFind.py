class UnionFind:
    def __init__(self, n) -> None:
        self.components = n
        self.fa = list(range(n))
        self.rank = [1] * n

    def __str__(self) -> str:
        return " ".join(map(str, self.fa))

    def find(self, x):
        if self.fa[x] != x:
            self.fa[x] = self.find(self.fa[x])
        return self.fa[x]

    def union(self, x, y):
        fx, fy = self.find(x), self.find(y)
        if fx == fy:
            return False
        if self.rank[fy] > self.rank[fx]:
            fx, fy = fy, fx
        self.fa[fy] = fx
        self.rank[fx] += self.rank[fy]
        self.components -= 1
        return True

    def merge(self, x, y):
        fx, fy = self.find(x), self.find(y)
        self.rank[fy] += self.rank[fx]
        self.fa[fx] = fy

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)

    def all_is_connected(self):
        return self.components == 1

    def size(self, x):
        return self.rank[self.find(x)]
