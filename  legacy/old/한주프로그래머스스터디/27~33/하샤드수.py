def solution(x):
    array = list(str(x))
    num = 0
    for i in array:
        num += int(i)
    if x % num == 0:
        return True
    else:
        return False

x = 12
print(solution(x))