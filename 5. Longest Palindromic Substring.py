class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = len(s)
        if l in (0, 1):
            return s

        def expand_from(left: int, right: int):
            while left >= 0 and right < l and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1

        start = 0
        end = 0
        for i in range(l):
            sz = max(expand_from(i, i), expand_from(i, i + 1))
            if end - start < sz:
                start = i - (sz - 1) // 2
                end = i + sz // 2

        return s[start:end + 1]


print(Solution().longestPalindrome("babad"))
