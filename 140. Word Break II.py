from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        res = []

        def dfs(i, path):
            if len(s) == i:
                res.append(' '.join(path))

            for j in range(i, len(s)):
                tmp = s[i:j + 1]
                if tmp in wordDict:
                    dfs(j + 1, path + [tmp])

        dfs(0, [])
        return res


print(Solution().wordBreak(s="catsanddog", wordDict=["cat", "cats", "and", "sand", "dog"]))
