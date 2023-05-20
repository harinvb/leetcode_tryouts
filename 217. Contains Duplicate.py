from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq = set()
        for i in nums:
            if i in freq:
                return True
            freq.add(i)
        return False
