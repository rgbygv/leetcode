#[derive(Debug)]
pub struct UnionFind {
    fa: Vec<usize>,
    rank: Vec<i32>,
    comp: usize,
}
impl UnionFind {
    pub fn new(n: usize) -> Self {
        Self {
            fa: (0..n).collect(),
            rank: vec![1; n],
            comp: n,
        }
    }

    pub fn find(&mut self, mut x: usize) -> usize {
        let mut y = x;
        while y != self.fa[y] {
            y = self.fa[y];
        }
        while x != y {
            let next = self.fa[x];
            self.fa[x] = y;
            x = next;
        }
        y
    }

    pub fn union(&mut self, x: usize, y: usize) -> bool {
        let (mut fx, mut fy) = (self.find(x), self.find(y));
        if fx == fy {
            return false;
        }

        if self.rank[fx] < self.rank[fy] {
            swap(&mut fx, &mut fy);
        }
        self.fa[fy] = fx;
        self.rank[fx] += self.rank[fy];
        self.comp -= 1;
        true
    }
}
