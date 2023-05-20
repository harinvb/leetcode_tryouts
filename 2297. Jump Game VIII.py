from typing import List


class Solution:
    def minCost(self, nums: List[int], costs: List[int]) -> int:
        n = len(nums)
        next_possible_jumps = [i + 1 for i in range(n)]
        next_possible_jumps_max = [i + 1 for i in range(n)]
        min_mono = []
        max_mono = []
        for i in range(n - 1, -1, -1):
            if min_mono and min_mono[-1][0] <= nums[i]:
                while min_mono and min_mono[-1][0] <= nums[i]:
                    min_mono.pop()
            if max_mono and max_mono[-1][0] > nums[i]:
                while max_mono and max_mono[-1][0] > nums[i]:
                    max_mono.pop()
            if len(min_mono) > 0 and i != n - 1:
                next_possible_jumps[i] = min_mono[-1][1]
            if len(max_mono) > 0 and i != n - 1:
                next_possible_jumps_max[i] = max_mono[-1][1]
            min_mono.append((nums[i], i))
        print(next_possible_jumps)
        print(next_possible_jumps_max)

        return -1


print(Solution().minCost(nums=[3, 2, 4, 4, 1], costs=[3, 7, 6, 4, 2]))
