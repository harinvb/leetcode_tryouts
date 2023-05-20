from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        """row_to_zero = [False] * m
        col_to_zero = [False] * n
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row_to_zero[i] = True
                    col_to_zero[j] = True
        for i in range(m):
            if row_to_zero[i]:
                for j in range(n):
                    matrix[i][j] = 0
        for j in range(n):
            if col_to_zero[j]:
                for i in range(m):
                    matrix[i][j] = 0"""
        is_first_col_zero = False
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    if i == 0:
                        is_first_col_zero = True
                    else:
                        matrix[0][j] = 0
                        matrix[i][0] = 0
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(n):
                    matrix[i][j] = 0
        for j in range(n):
            if matrix[0][j] == 0:
                for i in range(m):
                    matrix[i][j] = 0
        if is_first_col_zero:
            for i in range(n):
                matrix[0][i] = 0
        # print(matrix)


print(Solution().setZeroes([[1, 2, 3, 4], [5, 0, 7, 8], [0, 10, 11, 12], [13, 14, 15, 0]]))
