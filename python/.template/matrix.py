def matrix_pow(a: list[list[int]], k: int) -> list[list[int]]:
    m = len(a)
    n = len(a[0])
    res = [[0] * n for _ in range(m)]
    for i in range(m):
        res[i][i] = 1
    while k > 0:
        if k & 1:
            res = matrix_mul(res, a)
        a = matrix_mul(a, a)
        k >>= 1
    return res


def matrix_mul(A: list[list[int]], B: list[list[int]], mod: int = 10**9 + 7):
    # m = len(a)
    # n = len(a[0])
    # p = len(b[0])
    # c = [[0] * p for _ in range(n)]
    # for i in range(m):
    #     for j in range(n):
    #         for k in range(p):
    #             c[i][k] = (c[i][k] + a[i][j] * b[j][k]) % mod

    # return c
    return [
        [sum(a * b % mod for a, b in zip(col, row)) % mod for col in zip(*B)]
        for row in A
    ]
