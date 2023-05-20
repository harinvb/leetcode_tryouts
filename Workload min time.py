workers = [5, 4, 3, 4, 4, 5]


def time_taken(val):
    res = 0
    for idx, w in enumerate(workers):
        res += abs(w - val - idx - 1)
    return res


high = max(workers)
print([time_taken(i) for i in range(high)])
low = 0
while low < high:
    mid = low + (high - low) // 2
    if time_taken(mid) < time_taken(mid + 1):
        high = mid
    else:
        low = mid + 1
print(time_taken(low), low)
