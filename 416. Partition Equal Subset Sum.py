from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums.sort()
        total_sum = sum(nums)
        cur_sum = 0
        for i in nums:
            cur_sum += i
            total_sum -= i
            if cur_sum == total_sum:
                return True
        return False
