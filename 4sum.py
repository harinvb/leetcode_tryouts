from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        num_len = len(nums)
        result = set()
        for i in range(0, num_len - 3):
            for j in range(i + 1, num_len - 2):
                curr_2sum = nums[i] + nums[j]
                left, right = j + 1, num_len - 1
                while left < right:
                    tot_sum = curr_2sum + nums[left] + nums[right]
                    if tot_sum == target: result.add((nums[i], nums[j], nums[left], nums[right]))
                    if tot_sum <= target:
                        left += 1
                    else:
                        right -= 1
        res_list = []
        for i in result:
            res_list.append(list(i))
        return res_list
