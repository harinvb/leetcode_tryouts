class Solution:
    def punishmentNumber(self, n: int) -> int:
        # Generate the magic numbers between 1 and 1000
        # def backtrack(idx,s):
        #     if idx>=len(s):
        #         return [0]
        #     pos = []
        #     for i in range(idx,len(s)):
        #         x = int(s[idx:i+1])
        #         ret = backtrack(i+1,s)
        #         for j in ret:
        #             pos.append(x + j)
        #     return pos
        # for n in range(1000+1):
        #     if n in set(backtrack(0,str(n*n))):
        #         print(n,end=',')
        s = {1, 9, 10, 36, 45, 55, 82, 91, 99, 100, 235, 297, 369, 370, 379, 414, 657, 675, 703, 756, 792, 909, 918,
             945, 964, 990, 991, 999, 1000}
        res = 0
        for i in range(n + 1):
            if i in s:
                res += (i * i)
        return res
