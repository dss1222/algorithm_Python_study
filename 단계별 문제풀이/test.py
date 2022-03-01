n = int(input())
fac = 1
if n > 0:
    for number in range(1, n+1):
        fac *= number

print(fac)