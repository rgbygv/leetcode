# Created by Jones at 2024/05/01 15:10
# leetgo: 1.4.5
# https://leetcode.cn/problems/online-election/

from typing import *
from leetgo_py import *

from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from functools import cache, cmp_to_key, lru_cache, reduce
from heapq import heapify, heappop, heappush, heappushpop, heapreplace
from icecream import ic
from itertools import accumulate, chain, count, pairwise, zip_longest
from math import ceil, comb, floor, gcd, inf, isqrt, lcm, log2, perm, sqrt
from operator import xor
from pprint import pprint
from string import ascii_lowercase
from typing import List, Optional

# @lc code=begin


class TopVotedCandidate:
    # - `1 <= persons.length <= 5000`
    # - `times.length == persons.length`
    # - `0 <= persons[i] < persons.length`
    # - `0 <= times[i] <= 10⁹`
    # - `times` is sorted in a strictly increasing order.
    # - `times[0] <= t <= 10⁹`
    # - At most `10⁴` calls will be made to `q`.

    def __init__(self, persons: List[int], times: List[int]):
        # if we store each votes at each time, O(n * n)
        # so we store votes for each person, O(n * m)
        # we compute the anwser here

        cnt = Counter()
        last = -1
        res = []

        for p in persons:
            cnt[p] += 1
            if cnt[p] >= cnt[last]:
                last = p
                res.append(p)
            else:
                res.append(last)
        self.times = times
        self.res = res

    def q(self, t: int) -> int:
        # now we can query each person, O(n * m)
        # so we should compute the answer in __init__
        i = bisect_right(self.times, t) - 1
        return self.res[i]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    constructor_params = split_array(params[0])
    persons: List[int] = deserialize("List[int]", constructor_params[0])
    times: List[int] = deserialize("List[int]", constructor_params[1])
    obj = TopVotedCandidate(persons, times)

    for i in range(1, len(ops)):
        match ops[i]:
            case "q":
                method_params = split_array(params[i])
                t: int = deserialize("int", method_params[0])
                ans = serialize(obj.q(t))
                output.append(ans)

    print("\noutput:", join_array(output))
