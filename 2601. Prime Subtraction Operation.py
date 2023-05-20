import bisect
from math import isqrt
from typing import List


class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        def primes_between(end=max(nums)) -> List[int]:
            is_num_prime = [True] * (end + 1)
            is_num_prime[0] = is_num_prime[1] = False
            for i in range(2, isqrt(end) + 1):
                if is_num_prime[i]:
                    for j in range(i * i, end + 1, i):
                        is_num_prime[j] = False
            return [num for num, is_prime in enumerate(is_num_prime) if is_prime]

        primes_in_between = primes_between()
        nums = [0] + nums
        for i in range(1, len(nums)):
            if primes_in_between:
                target = nums[i] - nums[i - 1] - 1
                target_idx = bisect.bisect_right(primes_in_between, target) - 1
                if target_idx < len(primes_in_between) and primes_in_between[target_idx] <= target:
                    nums[i] -= primes_in_between[target_idx]
            if nums[i] <= nums[i - 1]:
                return False
        return True


s = Solution()
print(s.primeSubOperation([4, 9, 6, 10]))  # True
print(s.primeSubOperation([6, 8, 11, 12]))  # True
print(s.primeSubOperation([5, 8, 3]))  # False
print(s.primeSubOperation([4, 9, 6, 10, 1]))  # False
print(s.primeSubOperation([4, 9, 1, 10]))  # False
print(s.primeSubOperation([3]))  # True
