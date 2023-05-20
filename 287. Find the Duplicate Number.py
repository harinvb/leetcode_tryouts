from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        a = set(nums)
        return (sum(nums) - sum(a)) // (len(nums) - len(a))


print(Solution().findDuplicate([1, 3, 4, 2, 2]))
