class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0: return 0
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n + 1):
            if i % 2 == 0:
                dp[i] = dp[i // 2]
            else:
                x = (i - 1) // 2
                dp[i] = dp[x] + dp[x + 1]
        return max(dp)


print(Solution().getMaximumGenerated(100))
