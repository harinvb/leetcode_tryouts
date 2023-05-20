from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_so_far = nums[0]
        max_so_far = nums[0]
        result = nums[0]
        for i in range(1, len(nums)):
            min_so_far, max_so_far = min(nums[i], nums[i] * min_so_far, nums[i] * max_so_far), max(nums[i],
                                                                                                   nums[i] * min_so_far,
                                                                                                   nums[i] * max_so_far)
            result = max(result, max_so_far)
        return result


print(Solution().maxProduct([1, 2, -1, -2, 0]))
