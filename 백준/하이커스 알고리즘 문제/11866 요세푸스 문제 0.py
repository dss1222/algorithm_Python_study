from collections import deque

n, k = map(int, input().split())
s = deque([i for i in range(1, n+1)])

print('<', end='')
while s:
    for i in range(k - 1):
        s.append(s[0])
        s.popleft()
    print(s.popleft(), end='')
    if s:

        print(', ', end='')
print('>')