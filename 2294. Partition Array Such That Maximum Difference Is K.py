from bisect import bisect_right
from typing import List

from sortedcontainers import SortedList


class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        l = len(nums)
        res = 0
        while i < l:
            end = bisect_right(nums, nums[i] + k, i + 1)
            if end < l and nums[end] - nums[i] > k:
                end -= 1
            i = end + 1
            res += 1
        return res


print(Solution().partitionArray([2, 2, 4, 5], 3))
SortedList()
