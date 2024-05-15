from functools import lru_cache


def digit_dp(n):
    s = str(n)

    @lru_cache(None)
    def dfs(i: int, is_num: bool, limit: bool):
        if i == len(s):
            return int(is_num)
        res = 0
        if not is_num:
            res = dfs(i + 1, False, False)

        low = 0 if is_num else 1
        up = 9 if not limit else int(s[i])
        for x in range(low, up + 1):
            res += dfs(i + 1, True, limit and x == up)
        return res

    return dfs(0, False, True)
