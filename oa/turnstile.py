def solution(n, arrtime, direction):
    enter, exit = [], []
    res = [0] * n
    for i, t in enumerate(arrtime):
        if dir[i] == 1:
            exit.append((t, i))
        else:
            enter.append((t, i))

    time, last = 0, -1
    while exit or enter:
        if exit and exit[0][0] <= time and (last != 0 or not enter or (last == 0 and enter[0][0] < time)):
            res[exit[0][1]] = time
            last = 1
            exit.pop(0)
        elif enter and enter[0][0] <= time:
            res[enter[0][1]] = time
            last = 0
            enter.pop(0)
        else:
            last = -1
        time += 1
    return res