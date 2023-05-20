class Solution:
    def appealSum(self, s: str) -> int:
        n = len(s)
        appeal_dp = [[0] * n for _ in range(n)]
        state_dp = [[0] * n for _ in range(n)]

        def flip_bit(num: int, position: int):
            return num ^ (1 << position)

        def no_of_set_bits(num: int):
            res = 0
            while num > 0:
                res += num & 1
                num >>= 1
            return res

        def combine_states(a: int, b: int):
            return a | b

        final_appeal = 0
        for i in range(n, -1, -1):
            for j in range(i, n):
                if i == j:
                    state_dp[i][j] = flip_bit(0, ord(s[j]) - ord('a'))
                    appeal_dp[i][j] = 1
                else:
                    state_dp[i][j] = combine_states(state_dp[i][j - 1], state_dp[i + 1][j])
                    appeal_dp[i][j] = no_of_set_bits(state_dp[i][j])
                final_appeal += appeal_dp[i][j]
        return final_appeal
