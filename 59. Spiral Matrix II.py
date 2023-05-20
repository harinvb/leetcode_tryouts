from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result = [[0] * n for _ in range(n)]
        left = top = 0
        bottom = right = n - 1
        cur = 1
        while cur < (n * n) + 1:
            for col in range(left, right + 1):
                result[top][col] = cur
                cur += 1
            for row in range(top + 1, bottom + 1):
                result[row][right] = cur
                cur += 1
            if top != bottom:
                for col in range(right - 1, left - 1, -1):
                    result[bottom][col] = cur
                    cur += 1
            if left != right:
                for row in range(bottom - 1, top, -1):
                    result[row][left] = cur
                    cur += 1
            left, right, bottom, top = left + 1, right - 1, bottom - 1, top + 1
        return result


print(Solution().generateMatrix(3))
