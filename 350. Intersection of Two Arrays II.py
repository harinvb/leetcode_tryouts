from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        cnt = [0 for _ in range(1001)]
        for i in nums1: cnt[i] += 1
        res = []
        for i in nums2:
            if cnt[i]:
                res.append(i)
                cnt[i] -= 1
        return res
