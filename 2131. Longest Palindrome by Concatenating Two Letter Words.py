from collections import defaultdict
from typing import List


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        palindrome_map = defaultdict(int)
        res = 0
        palindromes = set()
        for word in words:
            rev = word[::-1]
            if rev in palindrome_map:
                palindrome_map[rev] += 1
                if word == rev:
                    palindromes.add(word)
            else:
                palindrome_map[rev] += 1
        print(palindrome_map)
        print(palindromes)
        for k, v in palindrome_map.items():
            palindrome_map[k], res = v % 2, res + 4 * (v // 2)
        for word in palindromes:
            if palindrome_map[word] >= 1:
                return 2 + res
        return res


print(
    Solution().longestPalindrome(["ab", "ty", "yt", "lc", "cl", "ab"]))
