class Solution:
    def countVowelStrings(self, r: int) -> int:
        last_fac = r + 5
        dp = [0] * last_fac
        dp[0] = 1
        for i in range(1, last_fac):
            dp[i] = i * dp[i - 1]
        return dp[last_fac - 1] // (dp[r] * dp[4])


# vowels = ['a', 'e', 'i', 'o', 'u']
# c = 0
# for i in itertools.combinations_with_replacement(vowels, 50): c += 1
# print(c)

s = Solution()
print(s.countVowelStrings(50))
