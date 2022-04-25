n, k = map(int, input().split())
arr = []
for i in range(n):
    arr.append(int(input()))

count = 0
cnt=0
for i in reversed(range(n)):
    count += k // arr[i]  # 카운트 값에 K를 동전으로 나눈 몫을 더해줌
    k = k % arr[i]  # K는 동전으로 나눈 나머지로 계속 반복
    # if k==0:
    #     break
    cnt += 1

print(count)
print(cnt)
