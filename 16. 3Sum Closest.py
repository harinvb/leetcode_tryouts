from bisect import bisect_left
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums_len = len(nums)
        nums.sort()
        curr_possible_sum = 10_00_00
        for i in range(0, nums_len - 2):
            for j in range(i + 1, nums_len - 1):
                req = target - (nums[i] + nums[j])
                position = bisect_left(nums, req, j + 1)
                if position == nums_len: position -= 1
                curr_sum = nums[i] + nums[j] + nums[position]
                if abs(curr_sum - target) < abs(curr_possible_sum - target):
                    curr_possible_sum = curr_sum
        return curr_possible_sum
