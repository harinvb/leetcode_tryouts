class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        s_char = [i for i in s]
        l = len(s)
        for i in range(l//2):
            s_char[i] = min(s[i],s[-i-1])
            s_char[l-i-1] = min(s[i],s[-i-1])
            # print(s_char)
        return ''.join(s_char)