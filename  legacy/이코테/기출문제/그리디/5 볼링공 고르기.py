# n, m = map(int, input().split())
# ball = list(map(int,input().split()))
#
# answer = 0
# for i in range(n-1):
#     for j in range(i+1, n):
#         if ball[i] != ball[j]:
#             answer += 1
#
# print(answer)

n, m = map(int, input().split())
data = list(map(int,input().split()))

array = [0] * 11
result = 0
for x in data:
    array[x] += 1

for i in range(1, m+1):
    n -= array[i]
    result += array[i] * n

print(result)