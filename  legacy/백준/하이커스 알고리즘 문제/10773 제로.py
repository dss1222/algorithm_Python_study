import sys
from collections import deque
n = int(sys.stdin.readline())
q = deque()
for i in range(n):
    N = int(sys.stdin.readline())
    if N != 0:
        deque.append(q, N)
    else:
        deque.pop(q)

print(sum(q))