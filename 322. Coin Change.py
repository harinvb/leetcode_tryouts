from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        max_val = amount + 1
        dp = [max_val for _ in range(amount + 1)]
        dp[0] = 0
        for i in range(amount + 1):
            for j in coins:
                if j <= i:
                    dp[i] = min(dp[i], dp[i - j] + 1)
        return -1 if dp[amount] >= max_val else dp[amount]


s = Solution()
print(s.coinChange([3, 7, 405, 436], 8839))
