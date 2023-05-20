from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        sp = 0
        for i, j in enumerate(nums):
            if j != 0:
                nums[i], nums[sp] = nums[sp], nums[i]
                sp += 1


a = [0, 1, 2, 1, 0]
Solution().moveZeroes(a)
print(a)

print(a)
