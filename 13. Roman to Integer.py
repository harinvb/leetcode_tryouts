class Solution:
    roman_map: dict[str, int] = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    def romanToInt(self, s: str) -> int:
        res = 0
        i = 0
        l = len(s)
        while i < l:
            if i < l - 1 and self.roman_map[s[i]] < self.roman_map[s[i + 1]]:
                res += self.roman_map[s[i + 1]] - self.roman_map[s[i]]
                i += 1
            else:
                res += self.roman_map[s[i]]
            i += 1
        return res


print(Solution().romanToInt("MCMXCIV"))
