from math import sqrt
from typing import List


class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        points = set()

        def distance_from(from_x, from_y, to_x, to_y):
            return sqrt(pow(from_x - to_x, 2) + pow(from_y - to_y, 2))

        def generate_possible_points(x, y, r):
            for i in range(x - r, x + r + 1):
                for j in range(y - r, y + r + 1):
                    if distance_from(x, y, i, j) <= r:
                        points.add((i, j))

        for a, b, r in circles:
            generate_possible_points(a, b, r)
        return len(points)


print(Solution().countLatticePoints(
    [[8, 9, 6], [9, 8, 4], [4, 1, 1], [8, 5, 1], [7, 1, 1], [6, 7, 5], [7, 1, 1], [7, 1, 1], [5, 5, 3]]))
