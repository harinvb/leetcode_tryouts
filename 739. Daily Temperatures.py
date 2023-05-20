from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        max_stack = []
        l = len(temperatures)
        res = [0] * l
        for i in range(l):
            n = 1
            while len(max_stack) > 0 and temperatures[max_stack[-1]] < temperatures[i]:
                top_idx = max_stack.pop()
                res[top_idx] = i - top_idx
            max_stack.append(i)
        return res


print(Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
