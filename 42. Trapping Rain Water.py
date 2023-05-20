from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left_arr = []
        right_arr = []
        left_max = 0
        right_max = 0
        l = len(height)
        for i in range(l):
            left_max = max(left_max, height[i])
            right_max = max(right_max, height[l - i - 1])
            left_arr.append(left_max)
            right_arr.append(right_max)
        right_arr.reverse()
        res = 0
        for i in range(l):
            res += min(left_arr[i], right_arr[i]) - height[i]
        return res


print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
