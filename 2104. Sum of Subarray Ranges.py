from typing import List


class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        min_dp = [[0] * n for _ in range(n)]
        max_dp = [[0] * n for _ in range(n)]
        for i in range(n):
            min_dp[i][i] = nums[i]
            max_dp[i][i] = nums[i]
        res = 0
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                min_dp[i][j] = min(min_dp[i][j - 1], min_dp[i + 1][j])
                max_dp[i][j] = max(max_dp[i][j - 1], min_dp[i + 1][j])
                res += max_dp[i][j] - min_dp[i][j]
        return res
