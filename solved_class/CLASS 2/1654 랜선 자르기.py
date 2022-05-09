import sys

k, n = map(int, input().split())
arr = [int(sys.stdin.readline()) for _ in range(k)]

start, end = 1, max(arr)

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in arr:
        cnt += i // mid  # 랜선을 자른 수

    if cnt >= n:  # 랜선을 자른 수가 만들어야 될 랜선의 수보다 클 경우
        start = mid + 1
    else:  # 랜선을 자른 수가 만들어야될 랜선의 수보다 작은 경우
        end = mid - 1

print(end)
