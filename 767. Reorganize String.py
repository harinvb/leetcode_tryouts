from collections import Counter


class Solution:
    def reorganizeString(self, s: str) -> str:
        l = len(s)
        res = [''] * l
        idx = 0
        for f, c in sorted([(f, c) for c, f in Counter(s).items()], reverse=True):
            cf = f
            while cf:
                res[idx], cf, idx = c, cf - 1, idx + 2
                if idx >= l: idx = 1
        for i in range(l - 1):
            if res[i] == res[i + 1]: return ''
        return ''.join(res)


print(Solution().reorganizeString("aabba"))
