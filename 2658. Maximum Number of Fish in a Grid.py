from typing import List


class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            nonlocal grid
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
                return 0
            res, grid[i][j] = grid[i][j], 0
            res += dfs(i + 1, j)
            res += dfs(i - 1, j)
            res += dfs(i, j + 1)
            res += dfs(i, j - 1)
            return res

        m = len(grid)
        n = len(grid[0])
        max_fish = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    max_fish = max(max_fish, dfs(i, j))
        return max_fish


s = Solution()
print(s.findMaxFish([[0, 2, 1, 0], [4, 0, 0, 3], [1, 0, 0, 4], [0, 3, 2, 0]]))
