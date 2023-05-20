from typing import List


class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pr = [0] * (n + 1)
        sf = [0] * (n + 1)
        for i in range(n):
            pr[i + 1] = pr[i] | nums[i]
        for i in range(n - 1, -1, -1):
            sf[i] = sf[i + 1] | nums[i]
        ans = 0
        for i in range(n):
            cur = pr[i] | (nums[i] * 2 ** k) | sf[i + 1]
            ans = max(ans, cur)
        return ans


s = Solution()
print(s.maximumOr(nums=[8, 1, 2], k=2))
