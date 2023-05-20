from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        """hep = []
        for i in range(m):
            heappush(hep, (matrix[i][0], i, 0))
        while hep:
            cur, i, j = heappop(hep)
            if cur == target: return True
            if j < n - 1:
                heappush(hep, (matrix[i][j + 1], i, j + 1))
        return False"""
        # search space reduction
        i = m - 1
        j = 0
        while j < n and i >= 0:
            if matrix[i][j] > target:
                i -= 1
            elif matrix[i][j] < target:
                j += 1
            else:
                return True
        return False


print(Solution().searchMatrix(
    matrix=[[-1, 3]],
    target=3))
