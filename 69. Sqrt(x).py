class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = (x // 2) + 1
        while low < high:
            mid = low + (high - low) // 2
            if x <= (mid * mid):
                high = mid
            else:
                low = mid + 1
        return low if low * low <= x else low - 1


print(Solution().mySqrt(8))
