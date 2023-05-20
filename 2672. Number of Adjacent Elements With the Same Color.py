from typing import List


class Solution:

    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        nums = [0] * n
        c = 0
        res = []
        for idx, col in queries:
            prev = nums[idx - 1] if idx - 1 >= 0 else 0
            next = nums[idx + 1] if idx + 1 < n else 0
            if nums[idx] and nums[idx] == prev: c -= 1
            if nums[idx] and nums[idx] == next: c -= 1
            nums[idx] = col
            if nums[idx] == prev: c += 1
            if nums[idx] == next: c += 1
            res.append(c)
        return res
