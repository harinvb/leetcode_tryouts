from typing import List

PHONE_DICT = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'],
              '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}


class Solution:

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0: return []
        if len(digits) == 1 or digits in PHONE_DICT: return PHONE_DICT[digits]
        for i in range(0, len(digits) - 1):
            self.combine(digits[:i + 1], digits[i + 1])
        return PHONE_DICT[digits]

    def combine(self, left: str, right: str) -> None:
        combination_arr = []
        for i in PHONE_DICT[left]:
            for j in PHONE_DICT[right]:
                combination_arr.append(i + j)
        PHONE_DICT[left + right] = combination_arr


sol = Solution()
print(sol.letterCombinations('234'))
