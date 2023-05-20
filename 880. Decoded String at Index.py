class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        res = ''
        start = 0
        for i, c in enumerate(s):
            if c.isdigit():
                res += s[start:i]
                res += res * (int(c) - 1)
                start = i + 1
            if len(res) > k:
                return res[k - 1]
        if len(res) == 0:
            return s[k - 1]
        return res[k - 1]


s = Solution()
print(3 // 2 + 3 % 2)
