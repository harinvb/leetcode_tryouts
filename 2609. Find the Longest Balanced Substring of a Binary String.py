class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        """res = 0
        n = len(s)
        zc = oc = 0
        for right in range(n):
            if s[right] == '0' and (right == 0 or s[right - 1] == '1'):
                res = max(res, min(zc, oc) * 2)
                zc = 0
                oc = 0
            if s[right] == '0':
                zc += 1
            else:
                oc += 1
        res = max(res, min(zc, oc) * 2)
        return res"""
        res = '01'
        while res in s:
            res = f'0{res}1'
        return len(res) - 2


s = Solution()
print(s.findTheLongestBalancedSubstring("01000111"))
print(s.findTheLongestBalancedSubstring("00111"))
print(s.findTheLongestBalancedSubstring("111"))
print(s.findTheLongestBalancedSubstring("0110011"))
