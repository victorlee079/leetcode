import math

def solution(A):
    n = len(A)
    dpu = [0] * (n+1)
    dpd = [0] * (n+1)
    cnt = 0
    for i in range(1, n):
        if A[i] >= A[i - 1]:
            dpu[i] = dpu[i - 1] + 1
    for i in range(1, n):
        if A[i] <= A[i - 1]:
            dpd[i] = dpd[i - 1] + 1

    prevu, prevd = dpu[0], dpd[0]

    # Special Case for all equal
    if dpu == dpd:
        return n // 2

    for i in range(1, n+1):
        a = b = 0
        if dpu[i] < prevu and prevu > prevd:
            a = prevu // 2
        if dpd[i] < prevd and prevd > prevu:
            b = prevd // 2
        prevu, prevd = dpu[i], dpd[i]
        cnt += max(a, b)
    return cnt


print(solution([3, 3, 3, 3, 3, 3]))
print(solution([3, 4, 5, 6, 7, 8]))
print(solution([8, 7, 6, 5, 4, 3]))
print(solution([3, 4, 2, 6, 3]))
