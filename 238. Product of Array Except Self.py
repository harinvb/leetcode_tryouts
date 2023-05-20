from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zc = 0
        zi = 0
        non_zero_mul = 1
        l = len(nums)
        for i, n in enumerate(nums):
            if n == 0:
                zc += 1
                zi = i
            else:
                non_zero_mul *= n
        if zc > 1:
            return [0] * l
        elif zc == 1:
            res = [0] * l
            res[zi] = non_zero_mul
            return res
        else:
            for i in range(l):
                nums[i] = int(non_zero_mul / nums[i])
        return nums


s = Solution()
print(s.productExceptSelf([0, 1, 0, -3, 3]))
