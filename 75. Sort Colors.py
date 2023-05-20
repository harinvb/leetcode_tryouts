from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """zc = 0
        oc = 0
        for i in nums:
            if i==0:zc+=1
            elif i==1:oc+=1
        i = 0
        for _ in range(zc):
            nums[i] = 0
            i+=1
        for _ in range(oc):
            nums[i] = 1
            i+=1
        for _ in range(i,len(nums)):
            nums[i] = 2
            i +=1"""
        zero_pointer = 0
        two_pointer = len(nums) - 1
        curr = 0
        while curr <= two_pointer:
            if nums[curr] == 2:
                nums[curr], nums[two_pointer] = nums[two_pointer], nums[curr]
                two_pointer -= 1
            elif nums[curr] == 0:
                nums[curr], nums[zero_pointer] = nums[zero_pointer], nums[curr]
                zero_pointer += 1
                curr += 1
            else:
                curr += 1


a = [2, 1]
Solution().sortColors(a)
print(a)
