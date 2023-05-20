class Solution:
    map = {
        '(': ')',
        '{': '}',
        '[': ']'
    }

    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1: return False
        stack = []
        for c in s:
            if c in ('(', '{', '['):
                stack.append(c)
            elif len(stack) == 0 or self.map[stack.pop()] != c:
                return False
        return len(stack) == 0


sol = Solution()
print(sol.isValid("(){}"))
