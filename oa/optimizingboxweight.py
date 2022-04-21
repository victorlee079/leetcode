def solution(arr):
    arr.sort()
    total = sum(arr)
    weight_a = 0
    ans = []
    for i in range(len(arr)):
        weight_a += arr[i]
        ans.append(arr[i])
        if weight_a > total - weight_a:
            break
    return ans[::-1]