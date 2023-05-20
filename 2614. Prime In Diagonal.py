from functools import lru_cache
from typing import List


@lru_cache(None)
def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        res = 0
        n = len(nums)
        for i in range(n):
            if isPrime(nums[i][i]):
                res = max(res, nums[i][i])
            if isPrime(nums[i][n - i - 1]):
                res = max(res, nums[i][n - i - 1])
        return res


s = Solution()
print(s.diagonalPrime([[1, 2, 3], [5, 6, 7], [9, 13, 11]]))
print(s.diagonalPrime([[1, 2, 3], [5, 17, 7], [9, 11, 10]]))
