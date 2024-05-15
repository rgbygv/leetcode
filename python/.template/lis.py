from bisect import bisect_left


def lis(a):
    q = []
    for x in a:
        if not q or x > q[-1]:
            q.append(x)
        else:
            i = bisect_left(q, x)
            q[i] = x
    return len(q)
