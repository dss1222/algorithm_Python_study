def solution(n):
    x = round(n**0.5, 2)
    if x.is_integer():
        return int((x + 1) * (x + 1))
    else:
        return -1


n = 121
print(solution(n))
