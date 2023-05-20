from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        cur = [-1, 0]
        res = 0
        for interval in intervals:
            if cur[0] <= interval[0] < cur[1]:
                res += 1
            else:
                cur = interval
        return res
