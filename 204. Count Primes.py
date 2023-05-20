class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1: return 0
        prime_arr = [True] * (n)
        prime_arr[0] = False
        prime_arr[1] = False
        cur = 2
        while cur ** 2 < n:
            if prime_arr[cur]:
                for i in range(cur ** 2, n, cur):
                    prime_arr[i] = False
            cur += 1
        return sum(prime_arr)


print(Solution().countPrimes(13))
