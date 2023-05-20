from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        curr = intervals[0]
        for i in range(1, len(intervals)):
            ps, pe = curr
            cs, ce = intervals[i]
            if cs <= pe:
                curr = [cs, max(ce, pe)]
            else:
                res.append(curr)
                curr = [cs, ce]
        res.append(curr)
        return res


print(Solution().merge([[1, 4], [2, 3]]))
