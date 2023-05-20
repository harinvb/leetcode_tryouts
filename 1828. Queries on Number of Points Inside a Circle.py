from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        given_points = [(a, b) for a, b in points]
        given_points.sort()
        res: List[int] = []
        for a, b, r in queries:
            y_start, y_end = bisect_left(given_points, (a - r, b)), bisect_right(given_points, (a + r, b))
            x_start, x_end = bisect_left(given_points, (a, b - r)), bisect_right(given_points, (a, b + r))
            print(given_points[y_start:y_end], given_points[x_start:x_end])
            res.append(len(set(given_points[y_start:y_end]).union(given_points[x_start:x_end])))
        return res


print(Solution().countPoints([[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]], [[1, 2, 2], [2, 2, 2], [4, 3, 2], [4, 3, 3]]))
