import math

n = int(input())
answer = list(str(math.factorial(n)))
cnt = 0
for i in reversed(answer):
    if i == '0':
        cnt += 1
    else:
        break
print(cnt)