import sys
from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from heapq import heapify, heappop, heappush
from itertools import accumulate, groupby
from math import ceil, comb, floor, gcd, inf, lcm, log2, prod, sqrt
from string import ascii_lowercase

MOD = 10**9 + 7


def main():
    n = int(input())
    a = list(read_ints())


def input():
    return sys.stdin.readline().rstrip()


def read_ints():
    return map(int, input().split())


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        main()
