class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(num: int):
            res = 0
            while num > 0:
                num, digit = divmod(num, 10)
                res += digit ** 2
            return res

        tortoise = n
        hare = get_next(n)
        while hare != 1 and tortoise != hare:
            tortoise = get_next(tortoise)
            hare = get_next(get_next(hare))
        return hare == 1
