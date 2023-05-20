from math import sqrt, ceil


class Solution:
    int_max = pow(10, 4) + 1

    def numSquares(self, n: int) -> int:

        """
        dp = [int_max] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        for i in range(1, ceil(sqrt(n)) + 1):
            if dp[i] == int_max:
                sqr = i * i
                while sqr <= n:
                    dp[sqr] = 1
                    sqr *= sqr
        if dp[n] == 1:
            return 1
        for i in range(2, n + 1):
            if dp[i] == int_max:
                for j in range(i // 2):
                    dp[i] = min(dp[i], dp[i - j - 1] + dp[j + 1])
        return dp[n]"""

        perfect_squares = [i ** 2 for i in range(0, int(sqrt(n)) + 1)]
        dp = [self.int_max] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n + 1):
            for sqr in perfect_squares:
                if i < sqr: break
                dp[i] = min(dp[i], dp[i - sqr] + 1)
        return dp[n]


print(Solution().numSquares(41))

print(int(4.3), ceil(4.3))
s = {1, 2, 3}
