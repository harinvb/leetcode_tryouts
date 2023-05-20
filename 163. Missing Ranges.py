from typing import List


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        def add_str(low, up):
            if up - low >= 1:
                res.append(f'{low}->{up}')
            elif up == low:
                res.append(f'{low}')

        res = []
        nums.sort()
        prev = lower - 1
        l = len(nums)
        for i in range(l + 1):
            curr = nums[i] if i < l else upper + 1
            add_str(prev + 1, curr - 1)
            prev = curr
        return res


print(Solution().findMissingRanges([2], 0, 9))
