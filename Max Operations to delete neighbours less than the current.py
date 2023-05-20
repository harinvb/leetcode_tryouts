from collections import deque


class Solution:
    max_val = pow(2, 32)

    def maxOperations(self, arr: list[int]) -> int:
        stack = [self.max_val]
        arr.append(self.max_val)
        for i in range(len(arr) - 1):
            if not (stack[-1] == arr[i] - 1 or arr[i + 1] == arr[i] - 1):
                stack.append(arr[i])
        return len(arr) - len(stack)


print(Solution().maxOperations([1, 1, 1, 1, 1]))
