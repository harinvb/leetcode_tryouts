from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def dfs(x: int, y: int):
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == 0:
                return 0
            grid[x][y] = 0
            return 1 + dfs(x + 1, y) + dfs(x - 1, y) + dfs(x, y + 1) + dfs(x, y - 1)

        return max(dfs(i, j) for i in range(m) for j in range(n))
