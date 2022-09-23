import math

n = int(input())
dp = [0] * (n+1)

dp[1] = 1
temp = []
for i in range(2, n+1):
    if math.sqrt(i) % 1 == 0:
        dp[i] = 1
    else:
        for j in range(1, math.floor(math.sqrt(i))+1):
            temp.append(dp[i-(j**2)]+1)
        dp[i] = min(temp)
        temp = []

print(dp[n])
#실패