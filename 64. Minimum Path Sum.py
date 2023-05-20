from heapq import heappop, heappush
from typing import List

DIRECTIONS = [[0, 1], [1, 0]]


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        hep = [(grid[0][0], 0, 0)]
        dst_map = {}
        while hep:
            dst, i, j = heappop(hep)
            for a, b in DIRECTIONS:
                if i + a < m and j + b < n:
                    if dst + grid[i + a][j + b] < dst_map.get((i + a, j + b), float('inf')):
                        dst_map[(i + a, j + b)] = dst + grid[i + a][j + b]
                        heappush(hep, (dst + grid[i + a][j + b], i + a, j + b))
        return dst_map[(m - 1, n - 1)]


s = Solution()
print(s.minPathSum([[1, 2, 3], [4, 5, 6]]))
