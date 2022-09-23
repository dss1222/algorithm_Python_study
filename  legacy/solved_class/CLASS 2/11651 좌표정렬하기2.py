import sys
n = int(sys.stdin.readline())
so = []
for i in range(n):
    (a, b) = map(int, sys.stdin.readline().split())
    so.append((b, a))
so.sort()
for i in so:
    print(i[1], i[0])