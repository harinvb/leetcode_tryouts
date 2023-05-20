class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sz = len(s)
        if sz in (0, 1): return sz
        curr = set()
        l = 0
        r = 0
        max_pos = 1
        while r < sz:
            if s[r] not in curr:
                curr.add(s[r])
                r += 1
                max_pos = max(max_pos, len(curr))
            else:
                curr.remove(s[l])
                l += 1
        return max_pos


print(Solution().lengthOfLongestSubstring("pwwkew"))
