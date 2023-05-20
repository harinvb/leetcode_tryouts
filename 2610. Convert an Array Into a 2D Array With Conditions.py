from collections import Counter
from typing import List


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        cntr = Counter(nums)
        res = []
        while cntr:
            cur = list(cntr.keys())
            for i in cur:
                cntr[i] -= 1
                if cntr[i] == 0:
                    del cntr[i]
            res.append(cur)
        return res


s = Solution()
print(s.findMatrix([1, 2, 3, 4]))
