# even
# aaaa
# aa aa
# a aaa , aaa a
# a a a a
# a a aa
# aa a a
from typing import List


# odd
# aaaaa
# a aaaa , aaaa a
# aa aaa , aaa aa
# a a a a a
# aa a a a , a a a aa

class Solution:
    res: List[List[str]]
    dp: List[List[bool]]
    l: int

    def partition(self, s: str) -> list[list[str]]:
        self.l = len(s)
        self.dp = [[False] * self.l for _ in range(self.l + 1)]
        # to build palindrome sub sequence iteratively
        # for i in range(self.l):
        #     for j in range(i, -1, -1):
        #         if s[i] == s[j] and (i - j <= 1 or self.dp[j + 1][i - 1]):
        #             self.dp[j][i] = True
        self.res = []
        self._partition(s, 0, [])
        return self.res

    def _partition(self, s: str, start: int, cur_str_lst: List[str]):
        if start >= len(s):
            self.res.append(cur_str_lst[:])
        for end in range(start, self.l):
            # build recursively and split recursively
            if s[start] == s[end] and (end - start <= 1 or self.dp[start + 1][end - 1]):
                self.dp[start][end] = True
                self._partition(s, end + 1, cur_str_lst + [s[start:end + 1]])


s = 'aabaa'
print(Solution().partition(s))
