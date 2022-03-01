N = int(input())
count = 0
while N >= 0:
    if N % 5 == 0:
        count += int(N // 5) #정수 나누기  (소수점 버림)
        print(count)
        break
    N -= 3
    count += 1
else:
    print(-1)
