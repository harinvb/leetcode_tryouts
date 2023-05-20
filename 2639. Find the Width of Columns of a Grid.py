from typing import List


class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])
        res = []
        for i in range(n):
            cur = 0
            for j in range(m):
                cur = max(cur, len(str(grid[j][i])))
            res.append(cur)
        return res


s = Solution()
print(s.findColumnWidth([[1], [22], [333]]))
print(s.findColumnWidth([[-15, 1, 3], [15, 7, 12], [5, 6, -2]]))
