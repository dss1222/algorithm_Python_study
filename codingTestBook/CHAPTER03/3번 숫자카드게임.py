n, m = map(int, input().split())

result = 0
minr = []
for i in range(n):
    data = list(map(int, input().split()))
    minr.append(min(data))

print(max(minr))
