from typing import List


class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        max_ele = max(nums)
        l = len(nums)
        dp = [[0] * (max_ele + 2) for _ in range(l)]
        for i in range(l):
            for j in range(nums[i] + 1, max_ele + 1):
                dp[i][j] = dp[i][j - 1] + cost[i]
            for j in range(nums[i] - 1, 0, -1):
                dp[i][j] = dp[i][j + 1] + cost[i]
        min_cost = pow(2, 31)
        for i in range(1, max_ele + 1):
            curr_cost = 0
            for j in range(l):
                curr_cost += dp[j][i]
            min_cost = min(min_cost, curr_cost)
        return min_cost


print(Solution().minCost(nums=
                         [735103, 366367, 132236, 133334, 808160, 113001, 49051, 735598, 686615, 665317, 999793, 426087,
                          587000, 649989, 509946, 743518],
                         cost=
                         [724182, 447415, 723725, 902336, 600863, 287644, 13836, 665183, 448859, 917248, 397790, 898215,
                          790754, 320604, 468575,
                          825614]))
