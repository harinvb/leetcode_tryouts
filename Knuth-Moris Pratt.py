a = 'AAAAAABAAAA'
b = 'AABAA'


def strStr(haystack: str, needle: str):
    m = len(needle)
    n = len(haystack)
    lps = [0] * m

    def build_lps():
        prevLPS = 0
        cur = 1
        while cur < m:
            if needle[cur] == needle[prevLPS]:
                prevLPS += 1
                lps[cur] = prevLPS
                cur += 1
            elif prevLPS == 0:
                lps[cur] = 0
                cur += 1
            else:
                prevLPS = lps[prevLPS - 1]

    def search():
        haystack_ptr = 0
        needle_ptr = 0
        while haystack_ptr < n:
            if haystack[haystack_ptr] == needle[needle_ptr]:
                haystack_ptr, needle_ptr = haystack_ptr + 1, needle_ptr + 1
            elif needle_ptr == 0:
                haystack_ptr += 1
            else:
                needle_ptr = lps[needle_ptr - 1]
            if needle_ptr == m:
                return haystack_ptr - m
        return -1

    build_lps()
    return search()


print(strStr(a, b))
