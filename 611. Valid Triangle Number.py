from bisect import bisect_left
from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                rgt = bisect_left(nums, nums[i] + nums[j], j + 1)
                res += rgt - j - 1
        return res


print(Solution().triangleNumber([2, 2, 3, 4]))
