from typing import List


class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        freq_cntr = [0] * 50

        def add(n):
            if n >= 0: return
            freq_cntr[abs(n) - 1] += 1

        def get():
            cn = 0
            for i in range(-50, 0, 1):
                if freq_cntr[abs(i) - 1] > 0:
                    cn += freq_cntr[abs(i) - 1]
                if cn >= x:
                    return i
            return 0

        def remove(n):
            if n >= 0: return
            freq_cntr[abs(n) - 1] -= 1

        for i in range(k - 1):
            add(nums[i])
        res = []
        for i in range(k - 1, len(nums)):
            add(nums[i])
            res.append(get())
            remove(nums[i - k + 1])
        return res


s = Solution()
# print(s.getSubarrayBeauty([1, -1, -3, -2, 3], 3, 2))
print(s.getSubarrayBeauty([-1, -2, -3, -4, -5], 2, 2))
