from heapq import heappush, heappop
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        hep = []
        intervals.sort()
        res = 1
        heappush(hep, intervals[0][1])
        for start, end in intervals[1:]:
            prev_end = hep[0]
            if start < prev_end:
                res += 1
            else:
                heappop(hep)
            heappush(hep, end)
        return res


print(Solution().minMeetingRooms([[0, 30], [5, 10], [15, 20]]))
