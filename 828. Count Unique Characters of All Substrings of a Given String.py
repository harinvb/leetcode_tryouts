class Solution:
    def uniqueLetterString(self, s: str) -> int:
        len_of_s = len(s)
        res = 0
        for i in range(len_of_s):
            unique_set = set()
            non_unique_set = set()
            for j in range(i, len_of_s):
                if i == j:
                    unique_set.add(s[j])
                elif s[j] in unique_set:
                    unique_set.remove(s[j])
                    non_unique_set.add(s[j])
                elif s[j] not in unique_set and s[j] not in non_unique_set:
                    unique_set.add(s[j])
                res += len(unique_set)
        return res


print(Solution().uniqueLetterString("ABA"))
