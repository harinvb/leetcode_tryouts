from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def reverse(start: int, end: int, arr: List[int]):
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1

        n = len(nums) - 1
        if n == 0: return
        k %= (n + 1)
        reverse(0, n, nums)
        reverse(0, k - 1, nums)
        reverse(k, n, nums)
        # print(nums)


print(Solution().rotate(nums=[1, 2], k=3))
