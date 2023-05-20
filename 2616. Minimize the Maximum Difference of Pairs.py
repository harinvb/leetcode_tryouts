from collections import Counter
from typing import List


class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        cntr = Counter(nums)
        nums.sort(key=lambda x: (-cntr[x], x))
        res = 0
        for i in range(0, 2 * p, 2):
            res = max(res, nums[i + 1] - nums[i])
        return res


s = Solution()
print(s.minimizeMax(nums=[10, 1, 2, 7, 1, 3], p=2))
print(s.minimizeMax([0, 5, 3, 4], 0))
