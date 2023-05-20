from functools import lru_cache
from typing import List


class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                grid[i][j] %= k

        @lru_cache
        def backtrack(x: int, y: int) -> List[int]:
            if x < 0 or x == m or y < 0 or y == n:
                return []
            if x == m - 1 and y == n - 1:
                return [grid[x][y]]
            res = []
            for i in backtrack(x, y + 1):
                res.append(grid[x][y] + i)
            for i in backtrack(x + 1, y):
                res.append(grid[x][y] + i)
            return res

        ans = 0
        for i in backtrack(0, 0):
            ans += i % k == 0
        return ans


print(Solution().numberOfPaths(grid=[[5, 2, 4], [3, 0, 5], [0, 7, 2]], k=3))
