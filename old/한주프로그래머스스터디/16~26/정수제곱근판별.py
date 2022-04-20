import math

def solution(n):
    x = math.sqrt(n)
    if n % x == 0:
        return int((x + 1) * (x + 1))
    else:
        return -1


n = 121
print(solution(n))
