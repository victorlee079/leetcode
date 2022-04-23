def solution(str):
    n = len(str)
    for i in range(n // 2):
        if str[i] != 'a':
            return str[:i] + 'a' + str[i+1:]
    return str[:-1] + 'b' if n == 1 else ''
