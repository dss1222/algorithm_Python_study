n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n - 1]
second = data[n - 2]

result = 0

while True:
    for i in range(k):  # 가장 큰수를 k번 더하기
        if m == 0:  # m이 0이라면 반복문 탈출
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)
