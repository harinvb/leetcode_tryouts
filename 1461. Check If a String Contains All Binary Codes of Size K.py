class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        return len({s[i: i + k] for i in range(0, len(s) - k + 1)}) == 1 << k


sol = Solution()
print(sol.hasAllCodes(
    "00110",
    2))
