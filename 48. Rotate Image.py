from typing import List


class Solution:
    def rotate(self, a: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l = len(a)
        li = l - 1
        for i in range((l // 2) + (l % 2)):
            for j in range(l // 2):
                temp = a[li - j][i]
                a[li - j][i] = a[li - i][li - j]
                a[li - i][li - j] = a[j][li - i]
                a[j][li - i] = a[i][j]
                a[i][j] = temp


s = Solution()
c = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
s.rotate(c)
print(c)
