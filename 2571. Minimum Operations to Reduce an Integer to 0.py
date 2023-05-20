class Solution:
    def minOperations(self, n: int) -> int:
        res = 0
        while n != 0:
            a = bin(n)[2:]
            al = len(a)
            for i in range(al - 1, -1, -1):
                x = a[i]
                if x == '1':
                    if i > 0 and a[i - 1] == '1':
                        n += (1 << al - i - 1)
                        res += 1
                        break
                    if i == 0 or a[i - 1] == '0':
                        n -= (1 << al - i - 1)
                        res += 1
                        break
        return res


s = Solution()
print(s.minOperations(39))
print(s.minOperations(54))
