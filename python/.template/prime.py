from _LEETCODE import *


def find_primes(N: int):
    p = [True] * (N + 1)
    p[0] = p[1] = False
    for i in range(2, N + 1):
        if not p[i]:
            continue
        for j in range(2 * i, N + 1, i):
            p[j] = False
    return p


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    root = isqrt(n)
    for i in range(3, root + 1, 2):
        if n % i == 0:
            return False
    return True


# def is_prime(x: int) -> bool:
#     if x < 2:
#         return False
#     i = 2
#     while i * i <= x:
#         if x % i == 0:
#             return False
#         i += 1
#     return True
