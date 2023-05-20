from math import ceil


class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        b_len = len(b)
        a_len = len(a)
        lps = [0] * b_len
        prevLPS = 0
        cur = 1
        while cur < b_len:
            if b[prevLPS] == b[cur]:
                prevLPS += 1
                lps[cur] = prevLPS
                cur += 1
            elif prevLPS == 0:
                lps[cur] = prevLPS
                cur += 1
            else:
                prevLPS = lps[prevLPS - 1]
        a_ptr = 0
        b_ptr = 0
        while a_ptr < (a_len + b_len):
            if a[a_ptr % a_len] == b[b_ptr]:
                a_ptr, b_ptr = a_ptr + 1, b_ptr + 1
            elif b_ptr == 0:
                a_ptr += 1
            else:
                b_ptr = lps[b_ptr - 1]
            if b_ptr == b_len:
                return ceil(a_ptr / a_len)
        return -1


print(Solution().repeatedStringMatch(a="abcd", b="cdabcdab"))
