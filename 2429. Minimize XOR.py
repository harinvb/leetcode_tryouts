import time


class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        #
        # def get_ones(num):
        #     one_count = 0
        #     while num > 0:
        #         one_count += num & 1
        #         num >>= 1
        #     return one_count
        #
        # ones = get_ones(num2) - get_ones(num1)
        ones = bin(num2).count('1') - bin(num1).count('1')
        i = 0
        while i < 32 and ones != 0:
            ptr = 1 << i
            if not (num1 & ptr) and ones > 0:
                ones -= 1
                num1 ^= ptr
            elif (num1 & ptr) and ones < 0:
                ones += 1
                num1 ^= ptr
            i += 1
        return num1


strt = time.time_ns()
print(Solution().minimizeXor(91, 18))
print(time.time_ns() - strt)
