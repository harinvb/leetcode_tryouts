from bisect import bisect_left
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l = len(nums)
        res = set()
        for i in range(l - 1):
            for j in range(i + 1, l):
                target = 0 - (nums[i] + nums[j])
                left_idx = bisect_left(nums, target, j + 1)
                if left_idx < l and nums[left_idx] == target:
                    res.add((nums[i], nums[j], nums[left_idx]))
        return [[i, j, k] for i, j, k in res]


s = Solution()
print(s.threeSum([-1, 0, 1, 2, -1, -4]))
