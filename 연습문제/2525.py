H, M = map(int, input().split())
m = int(input())
M2 = M + m
while (M2 >= 60):
    if (M2 >= 60):
        M2 -= 60
        H += 1
        if (H == 24):
            H = 0
    else:
        M2 = M + m

print(H, M2)
