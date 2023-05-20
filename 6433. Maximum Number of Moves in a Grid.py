from typing import List


class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        res = [[0] * n for _ in range(m)]

        def dfs(i, j):

            if res[i][j] != 0:
                return res[i][j]
            for a, b in ((-1, 1), (0, 1), (1, 1)):
                x = i + a
                y = j + b
                if 0 <= x < m and 0 <= y < n:
                    if grid[i][j] < grid[x][y]:
                        res[i][j] = max(res[i][j], dfs(x, y) + 1)
            return res[i][j]

        ret = 0
        for k in range(m):
            dfs(k, 0)
            ret = max(ret, res[k][0])
        return ret


s = Solution()
print(s.maxMoves([[2, 4, 3, 5], [5, 4, 9, 3], [3, 4, 2, 11], [10, 9, 13, 15]]))
