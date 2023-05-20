class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 1 or n == 2:
            return k ** n
        prev, cur = k, k * k
        n -= 2
        while n > 0:
            prev, cur = cur, (k - 1) * (cur + prev)
            n -= 1
        return cur
