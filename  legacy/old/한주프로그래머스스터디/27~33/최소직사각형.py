def solution(sizes):
    for i in sizes:
        if i[0] < i[1]:
            i[0], i[1] = i[1], i[0]
    x = 0
    y = 0
    for i in sizes:
        if i[0] > x:
            x = i[0]
        if i[1] > y:
            y = i[1]
    return x * y


print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
