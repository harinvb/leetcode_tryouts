from math import ceil
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        hi = max(piles)
        if n == h:
            return hi
        lo = 1

        def get_hours(bananas_per_hour: int) -> int:
            return sum([ceil(pile / bananas_per_hour) for pile in piles])

        while lo < hi:
            mid = (lo + hi) // 2
            hours = get_hours(mid)
            if h < hours:
                lo = mid + 1
            else:
                hi = mid
        return lo


print(Solution().minEatingSpeed(piles=[3, 6, 7, 11], h=8))
