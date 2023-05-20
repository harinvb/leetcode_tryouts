from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return sum([1 for a, b in zip(sorted(heights), heights) if a != b])


sol = Solution()
print(sol.heightChecker([5, 1, 2, 3, 4]))
