from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        l = len(nums)
        freq = [0] * (l + 1)
        for i in nums:
            freq[i] += 1
        res = [0, 0]
        for i, j in enumerate(freq[1:]):
            if j == 0:
                res[1] = i + 1
            if j > 1:
                res[0] = i + 1
        return res
