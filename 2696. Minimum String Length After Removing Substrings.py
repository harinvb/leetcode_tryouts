class Solution:
    def minLength(self, s: str) -> int:

        while 'AB' in s or 'CD' in s:
            iab = s.find('AB')
            if iab != -1:
                s = s[:iab] + s[iab + 2:]
                # print(s)
            icd = s.find('CD')
            if icd != -1:
                s = s[:icd] + s[icd + 2:]
                # print(s)

        return len(s)
