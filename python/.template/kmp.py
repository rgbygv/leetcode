# KMP 模板
def calc_max_match(s: str) -> list[int]:
    match = [0] * len(s)
    c = 0
    for i in range(1, len(s)):
        v = s[i]
        while c and s[c] != v:
            c = match[c - 1]
        if s[c] == v:
            c += 1
        match[i] = c
    return match


# KMP 模板
# 返回 text 中出现了多少次 pattern（允许 pattern 重叠）
def kmp_search(text: str, pattern: str) -> int:
    match = calc_max_match(pattern)
    match_cnt = c = 0
    for i, v in enumerate(text):
        v = text[i]
        while c and pattern[c] != v:
            c = match[c - 1]
        if pattern[c] == v:
            c += 1
        if c == len(pattern):
            match_cnt += 1
            c = match[c - 1]
    return match_cnt
