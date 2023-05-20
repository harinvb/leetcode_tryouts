from typing import List


class Solution:
    def maximizeGreatness(self, A: List[int]) -> int:
        A.sort()
        res = 0
        for a in A:
            if a > A[res]:
                res += 1
        return res


s = Solution()
print(s.maximizeGreatness([1, 3, 5, 2, 1, 3, 1]))
