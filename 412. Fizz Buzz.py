from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = ['' for _ in range(n + 1)]
        for i in range(3, n + 1, 3):
            res[i] += 'Fizz'
        for i in range(5, n + 1, 5):
            res[i] += 'Buzz'
        for i in range(1, n + 1):
            if res[i] == '': res[i] = str(i)
        return res[1:]
