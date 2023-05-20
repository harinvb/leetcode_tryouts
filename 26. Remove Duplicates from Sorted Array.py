from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow_ptr = 1
        for i in range(slow_ptr, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[slow_ptr] = nums[i]
                slow_ptr += 1
        return slow_ptr


a = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(Solution().removeDuplicates(a))
print(a)
