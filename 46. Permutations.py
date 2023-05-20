from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # # return list(itertools.permutations(nums, len(nums)))
        # n = len(nums)
        # res = []
        #
        # def backtrack(curr=0):
        #     if curr == n:
        #         res.append(nums[:])
        #     else:
        #         for i in range(curr, n):
        #             nums[curr], nums[i] = nums[i], nums[curr]
        #             backtrack(curr + 1)
        #             nums[i], nums[curr] = nums[curr], nums[i]
        #
        # backtrack()
        # return res
        # Heap's algorithm trail
        res = []

        def heaps_permute(n: int):
            if n == 1:
                res.append(nums[:])
                return
            heaps_permute(n - 1)
            for i in range(n - 1):
                if n % 2 == 0:
                    nums[i], nums[n - 1] = nums[n - 1], nums[i]
                else:
                    nums[0], nums[n - 1] = nums[n - 1], nums[0]
                heaps_permute(n - 1)

        heaps_permute(len(nums))
        return res


s = Solution()
print(s.permute([1, 2, 3]))
