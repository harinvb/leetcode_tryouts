class Solution:
    def numberOfWays(self, s: str) -> int:
        len_of_s = len(s)
        tot_zeros = s.count('0')
        tot_ones = len_of_s - tot_zeros
        cur_zeros = cur_ones = res = 0
        for i in range(len_of_s):
            if s[i] == '0':
                res += (cur_ones * (tot_ones - cur_ones))
                cur_zeros += 1
            else:
                res += (cur_zeros * (tot_zeros - cur_zeros))
                cur_ones += 1
        return res


print(Solution().numberOfWays("001101"))
