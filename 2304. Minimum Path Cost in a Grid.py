from typing import List


class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = grid[-1]

        for i in range(m - 2, -1, -1):
            new_dp = [float('inf')] * n
            for j in range(n):
                for nj in range(n):
                    new_dp[j] = min(new_dp[j], dp[nj] + moveCost[grid[i][j]][nj] + grid[i][j])
            dp = new_dp
        return min(dp)


s = Solution()
print(s.minPathCost(grid=[[5, 3], [4, 0], [2, 1]], moveCost=[[9, 8], [1, 5], [10, 12], [18, 6], [2, 4], [14, 3]]))
