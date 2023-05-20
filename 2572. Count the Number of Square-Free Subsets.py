import itertools
from collections import Counter
from typing import List

MOD = (10 ** 9) + 7


class Solution:
    def squareFreeSubsets(self, nums: List[int]) -> int:
        nums = Counter(filter(self.isSquareFree, nums))
        res = 0
        for i in range(1, len(nums) + 1):
            for comb in itertools.combinations(nums.keys(), i):
                cur = 1
                for j in comb:
                    cur *= (nums[j] % MOD)
                res += cur
        return res

    def isSquareFree(self, num: int):
        e = (num // 2) + 1
        for i in range(2, e):
            num /= i
            if num % i == 0: return False
        return True


s = Solution()
print(s.squareFreeSubsets([3, 4, 4, 5]))
