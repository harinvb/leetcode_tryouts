from functools import reduce
from operator import xor
from typing import List


class Solution:
    def doesValidArrayExist(self, d: List[int]) -> bool:
        return reduce(xor, d) == 0


s = Solution()
print(s.doesValidArrayExist([1, 1]))
