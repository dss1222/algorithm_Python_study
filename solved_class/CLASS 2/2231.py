n = int(input())
result = 0
for i in range(1, n+1):
    A = list(map(int, str(i)))
    S = i + sum(A)
    if(S ==  n):
        result = i
        break
print(result)
