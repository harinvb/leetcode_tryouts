from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest = 0
        for i in seen:
            if i - 1 not in seen:
                current = 0
                e = i
                while e in seen:
                    e += 1
                    current += 1
                longest = max(longest, current)
        return longest
