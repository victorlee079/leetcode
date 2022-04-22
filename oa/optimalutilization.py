import math


def solution(a, b, target):
    # n log n
    a.sort(key=lambda x:x[1])
    # m log m
    b.sort(key=lambda x:x[1])

    first, second = 0, len(b) - 1
    ans = []
    min_diff = math.inf

    # m + n
    while first < len(a) and second > -1:
        total = a[first][1] + b[second][1]
        if total > target:
            second -= 1
        elif total <= target:
            diff = target - total
            if diff == min_diff:
                ans.append([a[first][0], b[second][0]])
            elif diff < min_diff:
                ans.clear()
                ans.append([a[first][0], b[second][0]])
                min_diff = diff
            first += 1
    return ans


print(solution([[1, 3], [2, 5], [3, 7], [4, 10]], [[1, 2], [2, 3], [3, 4], [4, 5]], 10))
print(solution([[1, 8], [2, 15], [3, 9]], [[1, 8], [2, 11], [3, 12]], 20))
