# Created by Jones at 2024/01/26 15:57
# leetgo: dev
# https://leetcode.cn/problems/minimum-edge-weight-equilibrium-queries-in-a-tree/

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
from pprint import pprint
from string import ascii_lowercase
from typing import List, Optional

# @lc code=begin

class Solution:
    def minOperationsQueries(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        
        p = [-1] * n
        cnt = [[0] * 26 for _ in range(n)]
        d = [0] * (n+5)
        g = [[] for _ in range(n)]

        for x,y,w in edges:
            g[x].append((y,w-1))
            g[y].append((x,w-1))

        def dfs(x:int, fa:int):
            p[x] = fa
            for y, w in g[x]:
                if y == fa:
                    continue
                d[y] = d[x] + 1
                for i in range(26):
                    cnt[y][i] = cnt[x][i]
                cnt[y][w] += 1
                dfs(y, x)
        
        dfs(0, -1)
        

        N = 20
        pp = [p] + [[-1] * n for _ in range(N-1)]
        
        for i in range(1, N):
            for x in range(n):
                t = pp[i-1][x]
                if t != -1:
                    pp[i][x] = pp[i-1][t]
                
        # pprint(pp)
        res = []
        for X,Y in queries:
            x, y = X, Y
            total = d[x] + d[y]
            if d[x] > d[y]:
                x, y = y, x
            k = d[y] - d[x]
            for i in range(k.bit_length()):
                if (k >> i) & 1:
                    y = pp[i][y] 
            
            if x != y:
                for i in range(N-1,-1,-1):
                    px, py = pp[i][x], pp[i][y]
                    if px != py:
                        x, y = px, py
                x = pp[0][x]
            
            lca = x
            total -= 2 * d[lca]
            
            MAX = max(cnt[X][i] + cnt[Y][i] - 2 * cnt[lca][i] for i in range(26))
            # print(total , MAX, X, Y, lca)
            res.append(total - MAX)
        
        return res

            
                
                    

            
            

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    queries: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().minOperationsQueries(n, edges, queries)

    print("\noutput:", serialize(ans))
