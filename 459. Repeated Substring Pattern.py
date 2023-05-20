class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        if n == 1: return False
        if n == 2: return s[0] == s[1]
        lps = [0] * n
        prevLPS = 0
        cur = 1
        while cur < n:
            if s[cur] == s[prevLPS]:
                prevLPS += 1
                lps[cur] = prevLPS
                cur += 1
            elif prevLPS == 0:
                lps[cur] = 0
                cur += 1
            else:
                prevLPS = lps[prevLPS - 1]
        return lps[-1] > 0 and (n % (n - lps[-1]) == 0)


print(Solution().repeatedSubstringPattern("cdabcdab"))
