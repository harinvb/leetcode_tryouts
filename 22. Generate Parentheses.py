from typing import List


class Solution:
    res = []

    def generateParenthesis(self, n: int) -> List[str]:
        self.generate(n, n, '')
        return self.res

    def generate(self, open_brackets: int, closed_brackets: int, curr: str) -> None:
        if open_brackets == 0 and closed_brackets == 0:
            self.res.append(curr[:])
            return
        if closed_brackets > open_brackets:
            self.generate(open_brackets, closed_brackets - 1, curr + ')')
        if open_brackets > 0:
            self.generate(open_brackets - 1, closed_brackets, curr + '(')


s = Solution()
print(s.generateParenthesis(3))
