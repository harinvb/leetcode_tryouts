class Solution:
    dp_map = {'1': '11'}

    def countAndSay(self, n: int) -> str:
        if n == 1: return '1'

        def build(curr: str):
            if curr not in self.dp_map:
                self.dp_map[curr] = str(len(curr)) + curr[0]
            return self.dp_map[curr]

        res = self.countAndSay(n - 1)
        next_say = ''
        start = 0
        end = 1
        for i in range(1, len(res)):
            if res[i] == res[i - 1]:
                end += 1
            else:
                next_say += build(res[start:end])
                start = end
                end += 1
        next_say += build(res[start:end])
        self.dp_map[res] = next_say
        return next_say


print(Solution().countAndSay(30))
