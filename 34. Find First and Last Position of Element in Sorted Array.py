from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if len(nums) == 0:
            return [-1, -1]
        left = lower_bound(nums, 0, n - 1, target)
        if left == n or nums[left] != target:
            return [-1, -1]
        else:
            return [left, upper_bound(nums, left, n - 1, target) - 1]


def lower_bound(nums: List[int], start: int, end: int, target: int):
    while start < end:
        mid = start + (end - start) // 2
        if target <= nums[mid]:
            end = mid
        else:
            start = mid + 1
    return start


def upper_bound(nums: List[int], start: int, end: int, target: int):
    while start < end:
        mid = start + (end - start) // 2
        if target < nums[mid]:
            end = mid
        else:
            start = mid + 1
    if nums[start] == target: start += 1
    return start


print(Solution().searchRange([5, 7, 7, 8, 8, 10], 6))
