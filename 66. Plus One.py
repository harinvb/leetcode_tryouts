from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        propagate = True
        i = len(digits) - 1
        while propagate and i >= 0:
            if digits[i] != 9:
                digits[i] += 1
                propagate = False
            else:
                digits[i] = 0
            i -= 1
        if propagate:
            digits.insert(0, 1)
        return digits


print(Solution().plusOne([1, 2, 3]))
