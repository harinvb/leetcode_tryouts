import itertools

a = [7, 8, 5, 5, 9, 2, 2, 0, 1, 6]
a.sort()
j = 0
res = 0
prev_xor = 0
for i in a:
    prev_xor ^= i
    res += prev_xor
print(res)