class Solution:
    def robotWithString(self, s: str) -> str:
        res = ''
        stck = []
        for i in s:
            if len(stck) == 0 or stck[-1] < i:
                stck.append(i)
            else:
                while stck and stck[-1] > i:
                    res += stck.pop()
        while stck:
            res += stck.pop()
        return res
