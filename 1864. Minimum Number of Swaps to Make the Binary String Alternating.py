class Solution:
    def minSwaps(self, s: str) -> int:
        s_len = len(s)
        zero_count = s.count('0')
        one_count = s_len - zero_count
        if abs(zero_count - one_count) > 1:
            return -1

        def count_alternating_anomalies(start_val):
            anomalies = 0
            for i in s:
                anomalies += i != start_val
                start_val = '1' if start_val == '0' else '0'
            return anomalies // 2

        if one_count > zero_count:
            return count_alternating_anomalies('1')
        elif zero_count > one_count:
            return count_alternating_anomalies('0')
        return min(count_alternating_anomalies('1'), count_alternating_anomalies('0'))


print(Solution().minSwaps(
    "00011110110110000000000110110101011101111011111101010010010000000000000001101101010010001011110000001101111111110000110101101101001011000011111011101101100110011111110001100110001110000000001100010111110100111001001111100001000110101111010011001"))
