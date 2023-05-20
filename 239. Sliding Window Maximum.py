from heapq import heappush
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        hep = []
        for i in range(k):
            heappush(hep, nums[i])
        res = []
        for i in nums:
            
