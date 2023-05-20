import string
from collections import Counter
from typing import List


class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        def generate_substrings(given: str) -> List[str]:
            res = []
            l = len(given)
            for i in range(l):
                for j in range(i + 1, l + 1):
                    if i == 0 and j == l:
                        continue
                    res.append(given[i:j])
            return res

        cntr = Counter(generate_substrings(t))
        res = 0
        for each in generate_substrings(s):
            for position in range(len(each)):
                for i in string.ascii_lowercase:
                    if each[position] != i:
                        new_substring = each[:position] + i + each[position + 1:]
                        res += cntr[new_substring]
        return res


print(Solution().countSubstrings(s="aba", t="baba"))
