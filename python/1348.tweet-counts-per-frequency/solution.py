# Created by Jones at 2024/05/05 16:15
# leetgo: 1.4.6
# https://leetcode.cn/problems/tweet-counts-per-frequency/

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
from sortedcontainers import SortedList


class TweetCounts:
    """
    - `0 <= time, startTime, endTime <= 10⁹`
    - `0 <= endTime - startTime <= 10⁴`
    - There will be at most `10⁴` calls **in total** to `recordTweet` and `getTweetCountsPerFrequency`.
    """

    def __init__(self):
        self.record = defaultdict(SortedList)
        self.map = {"minute": 60, "hour": 60 * 60, "day": 60 * 60 * 24}

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.record[tweetName].add(time)

    def getTweetCountsPerFrequency(
        self, freq: str, tweetName: str, startTime: int, endTime: int
    ) -> List[int]:
        q = self.record[tweetName]
        res = []
        step = self.map[freq]

        for t in range(startTime, endTime + 1, step):
            i = q.bisect_left(t)
            j = q.bisect_right(min(t + step - 1, endTime + 1))
            res.append(j - i)
        return res

        # q.add(inf)
        # left = q.bisect_left(startTime)
        # right = q.bisect_right(endTime)

        # def calc(x: int, y: int):
        #     return (y - x + step) // step

        # if left == right:
        #     # no record between (s, e)
        #     return [0] * calc(startTime, endTime)
        # # (s..q[i]) 0
        # # (q[i]..q[i+1]) 1

        # if startTime < q[left]:
        #     res.extend([0] * calc(startTime, q[left] - 1))
        # cnt = 1
        # for i in range(left, right):
        #     res.extend([cnt] * calc(q[i], min(q[i + 1] - 1, endTime)))
        #     cnt += 1
        # q.pop()

        # return res


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    obj = TweetCounts()

    for i in range(1, len(ops)):
        match ops[i]:
            case "recordTweet":
                method_params = split_array(params[i])
                tweetName: str = deserialize("str", method_params[0])
                time: int = deserialize("int", method_params[1])
                obj.recordTweet(tweetName, time)
                output.append("null")
            case "getTweetCountsPerFrequency":
                method_params = split_array(params[i])
                freq: str = deserialize("str", method_params[0])
                tweetName: str = deserialize("str", method_params[1])
                startTime: int = deserialize("int", method_params[2])
                endTime: int = deserialize("int", method_params[3])
                ans = serialize(
                    obj.getTweetCountsPerFrequency(freq, tweetName, startTime, endTime)
                )
                output.append(ans)

    print("\noutput:", join_array(output))
