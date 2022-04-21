# A better way is to store the pointers to the index in h and v
# such that it does not need to check again
def storage_optimization(n, m, h, v):
    max_h = max_v = 0

    prev = 0
    for i in range(1, n+2):
        max_h = max(max_h, i - prev)
        if i not in h:
            prev = i

    prev = 0
    for i in range(1, m+2):
        max_v = max(max_v, i - prev)
        if i not in v:
            prev = i

    return max_h * max_v


print(storage_optimization(3, 2, [1, 2, 3], [1, 2]))
