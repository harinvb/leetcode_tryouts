from typing import List


class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        N = len(nums)
        m = N // 2
        l = 0
        r = m
        res = 0
        while l < m and r < N:
            if nums[r] >= 2 * nums[l]:
                res += 2
                l += 1
            r += 1
        return res


s = Solution()
# print(s.maxNumOfMarkedIndices(
#     [1, 78, 27, 48, 14, 86, 79, 68, 77, 20, 57, 21, 18, 67, 5, 51, 70, 85, 47, 56, 22, 79, 41, 8, 39, 81, 59, 74, 14,
#      45, 49, 15, 10, 28, 16, 77, 22, 65, 8, 36, 79, 94, 44, 80, 72, 8, 96, 78, 39, 92, 69, 55, 9, 44, 26, 76, 40, 77,
#      16, 69, 40, 64, 12, 48, 66, 7, 59, 10]))
print(s.maxNumOfMarkedIndices([3, 5, 2, 4]))
print(s.maxNumOfMarkedIndices([9, 2, 5, 4]))
print(s.maxNumOfMarkedIndices([7, 6, 8]))
# print(s.maxNumOfMarkedIndices([2, 3, 6, 7]))
# print(s.maxNumOfMarkedIndices([2, 4]))
# print(s.maxNumOfMarkedIndices([2, 3]))
# print(s.maxNumOfMarkedIndices([2]))
# print(s.maxNumOfMarkedIndices([2, 3, 4, 5, 10, 11, 12, 12, 12]))
# print(s.maxNumOfMarkedIndices(
#     [42, 83, 48, 10, 24, 55, 9, 100, 10, 17, 17, 99, 51, 32, 16, 98, 99, 31, 28, 68, 71, 14, 64, 29, 15, 40]))

# 12 11  10   -1
#    7  8  9  -1
# 6  5  4     -1
#    1  2  3  -1
# 1  2  3  4
