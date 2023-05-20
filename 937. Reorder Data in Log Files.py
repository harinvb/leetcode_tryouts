from typing import List

INT_OR_SPACE_SET = set('1234567890 ')


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit_logs = []
        letter_logs = []
        for log in logs:
            l = set(log[log.index(' '):])
            if l.issubset(INT_OR_SPACE_SET):
                digit_logs.append(log)
            else:
                letter_logs.append(log)
        return sorted(letter_logs, key=lambda _log: (_log[_log.index(' '):], _log)) + digit_logs


print(
    Solution().reorderLogFiles(["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo", "a2 act car"]))
