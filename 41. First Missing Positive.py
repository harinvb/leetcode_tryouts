from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        is_one_absent = True
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1
            elif nums[i] == 1:
                is_one_absent = False
        if is_one_absent:
            return 1
        for i in range(n):
            if nums[abs(nums[i]) - 1] > 0:
                nums[abs(nums[i]) - 1] *= -1
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        return -1


print(Solution().firstMissingPositive([3, 4, -1, 1]))
