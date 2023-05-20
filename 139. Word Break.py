from functools import lru_cache
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)

        @lru_cache
        def word_break(st: str):
            if st in wordDict:
                return True
            for i in range(len(s)):
                sub_str = st[:i + 1]
                if sub_str in wordDict:
                    if word_break(st[i + 1:]):
                        return True

        return True if word_break(s) else False


print(Solution().wordBreak(
    s="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
    wordDict=
    ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]))
