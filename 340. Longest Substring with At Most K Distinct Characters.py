class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0: return 0
        char_map = dict()
        slow_ptr = 0
        res = 0
        for i, c in enumerate(s):
            char_map[c] = i
            if len(char_map) > k:
                del_idx = min(char_map.values())
                char_map.pop(s[del_idx])
                slow_ptr = del_idx + 1
            res = max(res, i - slow_ptr + 1)
        return res


print(Solution().lengthOfLongestSubstringKDistinct("aa", 1))
