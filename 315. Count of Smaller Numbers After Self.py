from typing import List


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        next_smallest = [-1] * n
        stck = [(nums[-1], n - 1)]
        for i in range(n - 2, -1, -1):
            while len(stck) > 0 and stck[-1][0] >= nums[i]:
                stck.pop()
            if stck:
                next_smallest[i] = stck[-1][1]
            stck.append((nums[i], i))
        next_smallest[-1] = 0
        for i in range(n - 2, -1, -1):
            if next_smallest[i] == -1:
                next_smallest = 0
            else:
                next_smallest[i] = 1 + next_smallest[next_smallest[i]]
        return next_smallest


print(Solution().countSmaller([-1, -1, 3, 2, 6, -1, -2]))
