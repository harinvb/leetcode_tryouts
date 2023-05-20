from operator import xor
from typing import List


class Solution:

    def evalRPN(self, tokens: List[str]) -> int:
        stck = []
        for token in tokens:
            if token in ('*', '/', '+', '-'):
                a = stck.pop()
                b = stck.pop()
                if token == '*':
                    stck.append(a * b)
                elif token == '/':
                    is_negative = xor(a < 0, b < 0)
                    a = abs(a)
                    b = abs(b)
                    b //= a
                    if is_negative:
                        stck.append(-b)
                    else:
                        stck.append(b)
                elif token == '+':
                    stck.append(b + a)
                else:
                    stck.append(b - a)

            else:
                stck.append(int(token))
        return stck.pop()


print(Solution().evalRPN(["3", "-4", "+"]))
