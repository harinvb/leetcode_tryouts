from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0] * n for _ in range(m)]

        def dfs(x: int, y: int, prev: int):
            if x < 0 or x >= m or y < 0 or y >= n or matrix[x][y] <= prev:
                return 0
            if dp[x][y] > 0:
                return dp[x][y]
            dp[x][y] = 1 + max(dfs(x + 1, y, matrix[x][y]),
                               dfs(x - 1, y, matrix[x][y]),
                               dfs(x, y + 1, matrix[x][y]),
                               dfs(x, y - 1, matrix[x][y]))
            return dp[x][y]

        final_res = 0
        for i in range(m):
            for j in range(n):
                final_res = max(final_res, dfs(i, j, -1))
        return final_res


print(Solution().longestIncreasingPath([[9, 9, 4], [6, 6, 8], [2, 1, 1]]))
