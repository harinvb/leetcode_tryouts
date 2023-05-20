class Solution:
    def trailingZeroes(self, n: int) -> int:
        """res = 0
        for i in range(1, n + 1):
            if i % 5 == 0:
                num = i
                while num % 5 == 0:
                    num //= 5
                    res += 1
        return res"""
        res = 0
        i = 5
        while i <= n:
            res += n // i
            i *= 5
        return res


print(Solution().trailingZeroes(20))
