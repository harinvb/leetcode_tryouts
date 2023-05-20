class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        curr = 1
        res = 0
        A = ord('A') - 1
        for i in reversed(columnTitle):
            res += (ord(i) - A) * curr
            curr *= 26
        return res


print(Solution().titleToNumber('ZY'))
