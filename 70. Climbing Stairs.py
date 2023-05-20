class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        pp = p = 1
        n -= 1
        while n > 0:
            pp, p, n = p, pp + p, n - 1
        return p


s = Solution()
print(s.climbStairs(45))
