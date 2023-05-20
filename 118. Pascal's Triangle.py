from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for height in range(1, numRows):
            curr = [1]
            for i in range(height - 1):
                curr.append(res[height - 1][i] + res[height - 1][i + 1])
            curr.append(1)
            res.append(curr)
        return res


s = Solution()
print(s.generate(5))
