class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        sz = len(palindrome)
        if sz == 1: return ""
        replacement_idx = -1
        for i, c in enumerate(palindrome[:sz // 2]):
            if c > 'a':
                replacement_idx = i
                break
        if replacement_idx != -1:
            return palindrome[:replacement_idx] + 'a' + palindrome[replacement_idx + 1:]
        return palindrome[:sz - 1] + "b"


st = Solution()
print(st.breakPalindrome("aba"))
