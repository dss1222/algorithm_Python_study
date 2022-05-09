N, M = map(int,input().split())
numbers = list(map(int, input().split()))
result= 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if numbers[i] + numbers[j] + numbers[k] > M:
                continue
            else:
                result = max(result, numbers[i]+numbers[j]+numbers[k])
print(result)