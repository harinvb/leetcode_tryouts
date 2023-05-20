from collections import defaultdict
from itertools import product
from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        fh_sum_map = defaultdict(int)
        for t in product(nums1, nums2):
            fh_sum_map[sum(t)] += 1
        res = 0
        for t in product(nums3, nums4):
            target = -1 * (sum(t))
            if target in fh_sum_map:
                res += fh_sum_map[target]
        return res


print(Solution().fourSumCount(nums1=[0], nums2=[0], nums3=[0], nums4=[0]))
