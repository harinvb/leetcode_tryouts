import itertools
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """n = len(nums)
        res = []

        def backtrack(curr_arr=None, idx=0):
            if curr_arr is None:
                curr_arr = []
            if idx == n:
                res.append(curr_arr[:])
            else:
                # include
                curr_arr.append(nums[idx])
                backtrack(curr_arr, idx + 1)
                curr_arr.pop()
                # dont include
                backtrack(curr_arr, idx + 1)

        backtrack()
        return res"""
        res = []
        for i in range(len(nums) + 1):
            res += [list(j) for j in itertools.combinations(nums, i)]
        return res


s = Solution()
print(s.subsets([1, 2, 3]))
