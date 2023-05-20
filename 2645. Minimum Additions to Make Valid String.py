class Solution:
    def addMinimum(self, word: str) -> int:
        reference_word = 'abc'
        res = 0
        ref_idx = 0
        word += 'a'

        def increment():
            nonlocal ref_idx
            ref_idx += 1
            if ref_idx == 3:
                ref_idx = 0

        for c in word:
            while c != reference_word[ref_idx]:
                res += 1
                increment()
            increment()
        return res


s = Solution()
print(s.addMinimum("b"))
print(s.addMinimum("aaa"))
print(s.addMinimum("abc"))
print(s.addMinimum("ccc"))
print(s.addMinimum("c"))
