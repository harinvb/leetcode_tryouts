from functools import cache


class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        @cache
        def get_power(val: int) -> int:
            if val == 1: return 1
            return get_power(val // 2) + 1 if val % 2 == 0 else get_power((3 * val) + 1) + 1

        return sorted(range(lo, hi + 1), key=get_power)[k - 1]


print(Solution().getKth(1, 1000, 777))
